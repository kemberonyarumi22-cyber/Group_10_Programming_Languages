-- ============================================================
-- CCS 2105 - Question 10
-- Supermarket Checkout and Stock Consistency
-- ============================================================
-- Design idea:
--   * Each checkout counter is its own coroutine. It never touches
--     the stock table directly - it only *asks* for permission.
--   * The shared stock table lives in the scheduler's scope, so
--     there is exactly one authoritative copy of the truth.
--   * The scheduler resumes checkouts in round-robin order. Because
--     only one coroutine can ever be running at a time, the
--     check-then-update sequence in checkStock() can never be
--     interrupted midway by another checkout - this is what keeps
--     stock logically consistent without locks.
-- ============================================================

-- (b) Shared stock table - single source of truth, owned by the scheduler
local stock = {
    milk        = 12,
    bread       = 8,
    rice        = 15,
    sugar       = 6,
    cooking_oil = 4
}

-- Each checkout's shopping list: a sequence of {product, qty} requests
local checkoutData = {
    {
        name = "Checkout-1 (Amina)",
        cart = {
            { product = "milk",  qty = 3 },
            { product = "bread", qty = 2 },
            { product = "sugar", qty = 5 },   -- will be contested / may fail
        }
    },
    {
        name = "Checkout-2 (Otieno)",
        cart = {
            { product = "milk",        qty = 4 },
            { product = "rice",        qty = 6 },
            { product = "cooking_oil", qty = 2 },
        }
    },
    {
        name = "Checkout-3 (Wanjiru)",
        cart = {
            { product = "milk",  qty = 6 },   -- contests milk with 1 & 2
            { product = "sugar", qty = 2 },
            { product = "bread", qty = 3 },
        }
    }
}

-- (a) Each checkout is a coroutine that scans one product at a time and
--     yields the request out to the scheduler; it waits for the
--     scheduler's verdict before printing a receipt line and moving on.
local function checkoutProcess(name, cart)
    return coroutine.create(function()
        for _, item in ipairs(cart) do
            local approved, remaining = coroutine.yield(item.product, item.qty)

            if approved then
                print(string.format(
                    "[%s] Scanned %d x %-11s -> APPROVED  (stock left: %d)",
                    name, item.qty, item.product, remaining))
            else
                print(string.format(
                    "[%s] Scanned %d x %-11s -> REJECTED  (only %d in stock)",
                    name, item.qty, item.product, remaining))
            end
        end
        return "receipt closed for " .. name
    end)
end

-- (c) checkStock() is the single gatekeeper. It decides BEFORE any
--     update whether a purchase can proceed, then performs the update
--     as one atomic step (no coroutine can pre-empt this function).
local function checkStock(product, qty)
    local available = stock[product] or 0
    if available >= qty then
        stock[product] = available - qty
        return true, stock[product]
    else
        return false, available
    end
end

-- Build the coroutine list
local checkouts = {}
for _, c in ipairs(checkoutData) do
    table.insert(checkouts, { name = c.name, co = checkoutProcess(c.name, c.cart) })
end

print("=== Opening stock ===")
for _, p in ipairs({ "milk", "bread", "rice", "sugar", "cooking_oil" }) do
    print(string.format("  %-11s : %d", p, stock[p]))
end
print()
print("=== Interleaved checkout processing ===")

-- (d) Round-robin scheduler demonstrating interleaved execution.
--     Each pass gives every live checkout exactly one turn, so all
--     three counters progress "quasi-simultaneously" while stock
--     stays consistent, since real updates only ever happen one at a
--     time inside checkStock().
local pendingArgs = {}   -- results to feed back into each coroutine on its next resume
local active = #checkouts

while active > 0 do
    for _, entry in ipairs(checkouts) do
        if coroutine.status(entry.co) ~= "dead" then
            local args = pendingArgs[entry.co] or {}
            local ok, a, b = coroutine.resume(entry.co, table.unpack(args))

            if not ok then
                -- Error handling: never let one bad checkout crash the whole system
                print(string.format("[%s] ERROR: %s", entry.name, tostring(a)))
                active = active - 1
            elseif coroutine.status(entry.co) == "dead" then
                print(string.format("[%s] %s", entry.name, tostring(a)))
                active = active - 1
            else
                local product, qty = a, b
                local approved, remaining = checkStock(product, qty)
                pendingArgs[entry.co] = { approved, remaining }
            end
        end
    end
end

print()
print("=== Closing stock ===")
local negative_found = false
for _, p in ipairs({ "milk", "bread", "rice", "sugar", "cooking_oil" }) do
    print(string.format("  %-11s : %d", p, stock[p]))
    if stock[p] < 0 then negative_found = true end
end

print()
if negative_found then
    print("CONSISTENCY CHECK: FAILED - stock went negative!")
else
    print("CONSISTENCY CHECK: PASSED - no product ever went negative.")
end

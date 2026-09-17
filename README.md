# Checkout-Stock

## Group Members

* **Aluvi Ian** - C026-01-1064/2021
* **Kembero Collins Nyarumi** - C026-01-0964/2022
* **Karanja Cyrus Njonge** - C026-01-2610/2025

A Lua implementation of **Question 10: Supermarket Checkout and Stock Consistency** using coroutines.

## Overview

The program simulates multiple supermarket checkout counters running as Lua coroutines. Each checkout scans products and yields control to a central scheduler.

The scheduler maintains the shared stock and checks each purchase before updating it, ensuring that stock never becomes negative.

## Key Concepts

* **Coroutines:** Each checkout counter runs independently and yields after scanning an item.
* **Shared Stock:** A single stock table is maintained by the scheduler.
* **Stock Validation:** Purchases are approved only when sufficient stock is available.
* **Interleaving:** Checkouts are processed in round-robin order.
* **Consistency:** Stock updates cannot be interrupted because Lua coroutines use cooperative execution.

## Prerequisites

To run this project, you need to have Lua installed on your system.
* **Lua 5.4** (or compatible version).

You can download Lua from the [official website](https://www.lua.org/download.html) or install it via your system's package manager.

## Installation and Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/kemberonyarumi22-cyber/Checkout-Stock.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd Checkout-Stock
   ```

## Running the Program

Execute the Lua script from your terminal:

```bash
lua5.4 q10_checkout.lua
```

or depending on your environment, you can use:

```bash
lua q10_checkout.lua
```

## Result

The simulation demonstrates interleaved checkout execution while maintaining consistent stock. Requests that exceed the available quantity are rejected, and the final consistency check confirms that no product stock becomes negative.

## Files

* `q1010.docx` — Assignment write-up
* `files/` — Project files
* `README.md` — Project documentation

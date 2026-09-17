"""
PROGRAMMING LANGUAGES LAB - NAMES, BINDINGS AND SCOPES
GROUP 10 - SCOPE SCENARIO

GROUP MEMBERS:
1. Karanja Cyrus - C026-01-2610/2025
2. Kembero Collins Nyarumi - C026-01-0964/2022
3. Aluvi Ian - C026-01-1064/2021
"""

# Demonstrates CALL SCENARIO - Two different call sequences
# Run: python 4_scope_scenario.py

print("="*60)
print("SCOPE SCENARIO - Two Call Sequences")
print("="*60)

class Scope:
    def __init__(self, name, parent=None):
        self.name, self.parent, self.bindings = name, parent, {}
    def bind(self, k, v): self.bindings[k] = v

def resolve(name, env, call_chain):
    """Static: follows lexical parents | Dynamic: follows call stack"""
    # Static
    s_chain, curr, s_val = [], env, None
    while curr:
        s_chain.append(curr.name)
        if name in curr.bindings:
            s_val = curr.bindings[name]
            break
        curr = curr.parent
    
    # Dynamic
    d_chain, d_val = [], None
    for frame in reversed(call_chain):
        d_chain.append(frame["name"])
        if name in frame["bindings"]:
            d_val = frame["bindings"][name]
            break
    
    return s_val, d_val, s_chain, d_chain

# Setup static hierarchy
main = Scope("main")
main.bind("maxUnits", 8)

validate = Scope("validateRegistration", main)
validate.bind("maxUnits", 6)

check = Scope("checkPolicy", validate)  # No binding
check_direct = Scope("checkPolicy_direct", main)

# Call Sequence 1: main → validateRegistration → checkPolicy
print("\nSCENARIO 1: main → validateRegistration → checkPolicy")
call1 = [
    {"name": "main", "bindings": {"maxUnits": 8}},
    {"name": "validateRegistration", "bindings": {"maxUnits": 6}},
    {"name": "checkPolicy", "bindings": {}}
]
s_val, d_val, s_chain, d_chain = resolve("maxUnits", check, call1)
print(f"  STATIC:  {s_val}  (searched: {' → '.join(s_chain)})")
print(f"  DYNAMIC: {d_val}  (searched: {' → '.join(d_chain)})")

# Call Sequence 2: main → checkPolicy
print("\nSCENARIO 2: main → checkPolicy")
call2 = [
    {"name": "main", "bindings": {"maxUnits": 8}},
    {"name": "checkPolicy", "bindings": {}}
]
s_val, d_val, s_chain, d_chain = resolve("maxUnits", check_direct, call2)
print(f"  STATIC:  {s_val}  (searched: {' → '.join(s_chain)})")
print(f"  DYNAMIC: {d_val}  (searched: {' → '.join(d_chain)})")

print("\nKEY INSIGHT:")
print("  Dynamic scoping gives DIFFERENT results for same variable")
print("  depending on CALL SEQUENCE!")
print("  Static scoping is CONSISTENT regardless of call sequence.")
print("="*60)
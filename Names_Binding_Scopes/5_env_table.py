"""
PROGRAMMING LANGUAGES LAB - NAMES, BINDINGS AND SCOPES
GROUP 10 - REFERENCING ENVIRONMENT TABLE

GROUP MEMBERS:
1. Karanja Cyrus - C026-01-2610/2025
2. Kembero Collins Nyarumi - C026-01-0964/2022
3. Aluvi Ian - C026-01-1064/2021
"""

# Demonstrates REFERENCING ENVIRONMENT TABLE
# Run: python 5_env_table.py

print("="*60)
print("REFERENCING ENVIRONMENT TABLE")
print("="*60)

class Scope:
    def __init__(self, name, parent=None):
        self.name, self.parent, self.bindings = name, parent, {}
    def bind(self, k, v): self.bindings[k] = v

# Setup environments
main = Scope("main")
main.bind("maxUnits", 8)
main.bind("MIN_UNITS", 4)

val = Scope("validateRegistration", main)
val.bind("maxUnits", 6)
val.bind("local_counter", 0)

chk = Scope("checkPolicy", val)
chk.bind("status", "CHECK")

# Table data
table = []

# Point A: Inside main
visible_a = main.bindings
table.append(("Point A: Inside main()", visible_a))

# Point B: Inside validateRegistration
visible_b = {**main.bindings, **val.bindings}
table.append(("Point B: Inside validateRegistration()", visible_b))

# Point C: Inside checkPolicy
visible_c = {**main.bindings, **val.bindings, **chk.bindings}
table.append(("Point C: Inside checkPolicy()", visible_c))

# Display table
for point, bindings in table:
    print(f"\n{point}")
    print(f"  Visible Names: {list(bindings.keys())}")
    print(f"  Bindings:      {bindings}")

print("\n" + "="*60)
print("SCOPE vs LIFETIME EXPLANATION:")
print("""
  At Point A (main): 
    • maxUnits visible, MIN_UNITS visible
    • These are program-lifetime variables
  
  At Point B (validateRegistration):
    • Inherits main's variables (static scoping)
    • Adds local_counter (function-local)
    • local_counter exists only during function execution
  
  At Point C (checkPolicy):
    • Inherits from both main and validate
    • maxUnits is visible but bound to 8 (static)
    • status visible from current scope
""")
print("="*60)
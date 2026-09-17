"""
PROGRAMMING LANGUAGES LAB - NAMES, BINDINGS AND SCOPES
GROUP 10 - Course Registration & Scope Resolution Engine

GROUP MEMBERS:
1. Karanja Cyrus - C026-01-2610/2025
2. Kembero Collins Nyarumi - C026-01-0964/2022
3. Aluvi Ian - C026-01-1064/2021

DATE: August 12, 2026
COURSE: Programming Languages Lab
"""

# Demonstrates COMPLETE INTEGRATED EXECUTION
# Run: python 6_main_execution.py

print("="*60)
print("COMPLETE COURSE REGISTRATION & SCOPE ENGINE")
print("GROUP 10 - NAMES, BINDINGS AND SCOPES")
print("="*60)

from shared_data import STUDENTS, COURSES, MIN_UNITS, MAX_UNITS, CLEAR

# ---------- PART A: Validator ----------
print("\n" + "="*60)
print("PART A: REGISTRATION VALIDATOR")
print("="*60)

class Validator:
    total_validations = 0
    @classmethod
    def validate(cls, student):
        cls.total_validations += 1
        if student["clearance"] != CLEAR:
            return [], student["requested"], {"error": f"Clearance: {student['clearance']}"}
        requested = list(set(student["requested"]))
        total_units = sum(COURSES.get(c, {}).get("units", 0) for c in requested)
        if total_units < MIN_UNITS or total_units > MAX_UNITS:
            return [], requested, {"error": f"Units: {total_units} (limit: {MIN_UNITS}-{MAX_UNITS})"}
        accepted, rejected, reasons = [], [], {}
        for course in requested:
            prereqs = COURSES.get(course, {}).get("prereqs", [])
            if course not in COURSES:
                rejected.append(course); reasons[course] = "Invalid"
            elif all(p in student["completed"] for p in prereqs):
                accepted.append(course); reasons[course] = "✓ Accepted"
            else:
                rejected.append(course); reasons[course] = f"✗ Missing: {prereqs}"
        return accepted, rejected, reasons

for student in STUDENTS:
    print(f"\nStudent {student['id']}:")
    acc, rej, reasons = Validator.validate(student)
    print(f"  Accepted: {acc}")
    print(f"  Rejected: {rej}")
    if "error" in reasons:
        print(f"   {reasons['error']}")
    else:
        for c, r in reasons.items():
            print(f"  {c}: {r}")

print(f"\nTotal validations: {Validator.total_validations}")

# ---------- PART B & C: Scope Resolver ----------
print("\n" + "="*60)
print("PART B & C: SCOPE RESOLUTION")
print("="*60)

class Scope:
    def __init__(self, name, parent=None):
        self.name, self.parent, self.bindings = name, parent, {}
    def bind(self, k, v): self.bindings[k] = v

def resolve(name, env, call_chain):
    s_chain, curr, s_val = [], env, None
    while curr:
        s_chain.append(curr.name)
        if name in curr.bindings:
            s_val = curr.bindings[name]; break
        curr = curr.parent
    d_chain, d_val = [], None
    for frame in reversed(call_chain):
        d_chain.append(frame["name"])
        if name in frame["bindings"]:
            d_val = frame["bindings"][name]; break
    return s_val, d_val, s_chain, d_chain

main = Scope("main"); main.bind("maxUnits", 8)
validate = Scope("validateRegistration", main); validate.bind("maxUnits", 6)
check = Scope("checkPolicy", validate)

call1 = [
    {"name": "main", "bindings": {"maxUnits": 8}},
    {"name": "validateRegistration", "bindings": {"maxUnits": 6}},
    {"name": "checkPolicy", "bindings": {}}
]

print("\nScenario: main → validateRegistration → checkPolicy")
s_val, d_val, s_chain, d_chain = resolve("maxUnits", check, call1)
print(f"  STATIC:  {s_val}  (searched: {' → '.join(s_chain)})")
print(f"  DYNAMIC: {d_val}  (searched: {' → '.join(d_chain)})")

# ---------- PART D: Environment Table ----------
print("\n" + "="*60)
print("PART D: REFERENCING ENVIRONMENT TABLE")
print("="*60)

chk_direct = Scope("checkPolicy_direct", main)
chk_direct.bind("status", "CHECK")

visible_main = main.bindings
visible_val = {**main.bindings, **validate.bindings}
visible_chk = {**main.bindings, **validate.bindings, **chk_direct.bindings}

print("\nPoint A - main():")
print(f"  {visible_main}")
print("\nPoint B - validateRegistration():")
print(f"  {visible_val}")
print("\nPoint C - checkPolicy():")
print(f"  {visible_chk}")

# ---------- PART E: Comparison ----------
print("\n" + "="*60)
print("PART E: STATIC vs DYNAMIC SCOPING COMPARISON")
print("="*60)

print("""
STATIC SCOPING:
  • Resolved at compile-time from code structure
  • Predictable: just read the code
  • Readable: explicit parent-child relationships
  • Example: maxUnits = 8 (from main's lexical parent)

DYNAMIC SCOPING:
  • Resolved at run-time from call stack
  • Unpredictable: depends on execution path
  • Less readable: need to trace execution
  • Example: maxUnits = 6 (from validateRegistration's frame)

SCOPE vs LIFETIME:
  • total_validations: Program lifetime (class variable)
  • local_counter: Function scope (dies after function)
  • MIN_UNITS: Program lifetime (global constant)
  
KEY TAKEAWAY:
  Static scoping is preferred for predictability and readability.
  Dynamic scoping offers flexibility but sacrifices clarity.
  Most modern languages (Python, Java, C++) use static scoping.
""")

print("="*60)
print("END OF ASSIGNMENT")
print("GROUP 10 - Karanja Cyrus - C026-01-2610/2025, Kembero Collins Nyarumi - C026-01-0964/2022, Aluvi Ian - C026-01-1064/2021")
print("="*60)
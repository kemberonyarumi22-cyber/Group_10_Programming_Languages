"""
PROGRAMMING LANGUAGES LAB - NAMES, BINDINGS AND SCOPES
GROUP 10 - REGISTRATION VALIDATOR

GROUP MEMBERS:
1. Karanja Cyrus - C026-01-2610/2025
2. Kembero Collins Nyarumi - C026-01-0964/2022
3. Aluvi Ian - C026-01-1064/2021
"""

# Demonstrates REGISTRATION VALIDATOR with Scope vs Lifetime
# Run: python 2_registration_validators.py

print("="*60)
print("REGISTRATION VALIDATOR")
print("="*60)

from shared_data import STUDENTS, COURSES, MIN_UNITS, MAX_UNITS, CLEAR

class Validator:
    """Course registration validator"""
    total_validations = 0  # PROGRAM LIFETIME - exists for entire program
    
    @classmethod
    def validate(cls, student):
        """Validate registration - demonstrates scope vs lifetime"""
        cls.total_validations += 1
        local_counter = 0  # FUNCTION SCOPE - only exists during call
        
        # Check clearance
        if student["clearance"] != CLEAR:
            return [], student["requested"], {"error": f"Clearance: {student['clearance']}"}
        
        # Remove duplicates and calculate units
        requested = list(set(student["requested"]))
        total_units = sum(COURSES.get(c, {}).get("units", 0) for c in requested)
        local_counter += len(requested)  # Local variable in use
        
        # Check unit load
        if total_units < MIN_UNITS or total_units > MAX_UNITS:
            return [], requested, {"error": f"Units: {total_units} (limit: {MIN_UNITS}-{MAX_UNITS})"}
        
        # Check prerequisites
        accepted, rejected, reasons = [], [], {}
        for course in requested:
            local_counter += 1  # Local variable changes - still in scope
            prereqs = COURSES.get(course, {}).get("prereqs", [])
            if course not in COURSES:
                rejected.append(course)
                reasons[course] = "Invalid course"
            elif all(p in student["completed"] for p in prereqs):
                accepted.append(course)
                reasons[course] = "✓ Accepted"
            else:
                rejected.append(course)
                reasons[course] = f"✗ Missing: {prereqs}"
        
        # local_counter dies here (function scope ends)
        # total_validations persists (program lifetime)
        return accepted, rejected, reasons

# Run validator on all students
for student in STUDENTS:
    print(f"\nStudent: {student['id']}")
    print(f"  Requested: {student['requested']}")
    accepted, rejected, reasons = Validator.validate(student)
    print(f"  Accepted:  {accepted}")
    print(f"  Rejected:  {rejected}")
    if "error" in reasons:
        print(f"   {reasons['error']}")
    else:
        for course, reason in reasons.items():
            print(f"  {course}: {reason}")

print(f"\n{'='*60}")
print(f"SCOPE vs LIFETIME DEMONSTRATION:")
print(f"  total_validations (PROGRAM LIFETIME): {Validator.total_validations}")
print(f"  ✓ This persists across all function calls")
print(f"  local_counter (FUNCTION SCOPE): Dies after each validate() call")
print(f"  ✓ Try accessing 'local_counter' here - NameError!")
print(f"  Reason: local_counter goes out of scope when function returns")
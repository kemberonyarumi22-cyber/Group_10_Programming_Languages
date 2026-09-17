"""
PROGRAMMING LANGUAGES LAB - NAMES, BINDINGS AND SCOPES
GROUP 10 - Course Registration & Scope Resolution Engine

GROUP MEMBERS:
1. Karanja Cyrus - C026-01-2610/2025
2. Kembero Collins Nyarumi - C026-01-0964/2022
3. Aluvi Ian - C026-01-1064/2021

DATE: August 12, 2026
"""

# Shared data used across all components
MIN_UNITS, MAX_UNITS = 4, 8
CLEAR, PENDING, BLOCKED = "CLEAR", "PENDING", "BLOCKED"

STUDENTS = [
    {"id": "S001", "completed": ["CS101", "CS102"], "requested": ["CS201", "CS202"], "clearance": CLEAR},
    {"id": "S002", "completed": ["CS101"], "requested": ["CS201", "IT202"], "clearance": CLEAR},
    {"id": "S003", "completed": ["CS101", "CS102", "CS201"], "requested": ["CS301"], "clearance": PENDING},
    {"id": "S004", "completed": ["CS101", "SE101"], "requested": ["CS201", "SE202"], "clearance": CLEAR},
    {"id": "S005", "completed": ["CS101"], "requested": ["CS102", "CS201"], "clearance": CLEAR},
    {"id": "S006", "completed": ["CS101"], "requested": ["CS201", "CS202", "CS301"], "clearance": CLEAR},
    {"id": "S007", "completed": [], "requested": ["CS201"], "clearance": CLEAR}
]

COURSES = {
    "CS101": {"prereqs": [], "units": 3},
    "CS102": {"prereqs": ["CS101"], "units": 3},
    "CS201": {"prereqs": ["CS101", "CS102"], "units": 3},
    "CS202": {"prereqs": ["CS101", "CS102"], "units": 4},
    "CS301": {"prereqs": ["CS101", "CS102", "CS201"], "units": 3},
    "IT202": {"prereqs": ["CS101"], "units": 4},
    "SE101": {"prereqs": [], "units": 3},
    "SE202": {"prereqs": ["SE101", "CS101"], "units": 3}
}
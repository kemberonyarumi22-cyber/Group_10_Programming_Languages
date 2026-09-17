"""
PROGRAMMING LANGUAGES LAB - NAMES, BINDINGS AND SCOPES
GROUP 10 - NAMED CONSTANTS DEMONSTRATION

GROUP MEMBERS:
1. Karanja Cyrus - C026-01-2610/2025
2. Kembero Collins Nyarumi - C026-01-0964/2022
3. Aluvi Ian - C026-01-1064/2021
"""

# Demonstrates NAMED CONSTANTS - Program-lifetime values
# Run: python 1_named_constants.py

print("="*60)
print("NAMED CONSTANTS DEMONSTRATION")
print("="*60)

from shared_data import MIN_UNITS, MAX_UNITS, CLEAR

print(f"\nPolicy Constants (Program Lifetime):")
print(f"  MIN_UNITS = {MIN_UNITS}  (minimum course load)")
print(f"  MAX_UNITS = {MAX_UNITS}  (maximum course load)")
print(f"  CLEAR     = {CLEAR}      (clearance status)")

print(f"\nBenefits of Named Constants:")
print(f"  1. Single point of change - update MIN_UNITS once")
print(f"  2. Self-documenting code - meaning is clear")
print(f"  3. Error prevention - no typos in values")

print(f"\nMemory Addresses (show persistence):")
print(f"  MIN_UNITS address: {id(MIN_UNITS)}")
print(f"  MAX_UNITS address: {id(MAX_UNITS)}")

print(f"\nBinding Time: Compile-time/Definition-time")
print("="*60)
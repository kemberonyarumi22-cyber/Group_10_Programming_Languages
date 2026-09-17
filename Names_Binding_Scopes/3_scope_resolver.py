"""
PROGRAMMING LANGUAGES LAB - NAMES, BINDINGS AND SCOPES
GROUP 10 - SCOPE RESOLVER

GROUP MEMBERS:
1. Karanja Cyrus - C026-01-2610/2025
2. Kembero Collins Nyarumi - C026-01-0964/2022
3. Aluvi Ian - C026-01-1064/2021
"""

# Demonstrates STATIC vs DYNAMIC SCOPING - Core Resolver
# Run: python 3_scope_resolver.py

print("="*60)
print("SCOPE RESOLVER - Static vs Dynamic Scoping")
print("="*60)

class Scope:
    """Environment with lexical parent for static scoping"""
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.bindings = {}
    
    def bind(self, key, value):
        self.bindings[key] = value
    
    def lookup_static(self, key):
        """Static scoping: follows lexical parent chain"""
        if key in self.bindings:
            return self.bindings[key]
        if self.parent:
            return self.parent.lookup_static(key)
        return None

def resolve_static(name, env):
    """Pure static resolver - follows lexical parents"""
    chain, current = [], env
    while current:
        chain.append(current.name)
        if name in current.bindings:
            return current.bindings[name], chain
        current = current.parent
    return None, chain

def resolve_dynamic(name, call_chain):
    """Pure dynamic resolver - searches call stack"""
    chain = []
    for frame in reversed(call_chain):
        chain.append(frame["name"])
        if name in frame["bindings"]:
            return frame["bindings"][name], chain
    return None, chain

# Create test environment
main = Scope("main")
main.bind("maxUnits", 8)
main.bind("status", "GLOBAL")

validate = Scope("validateRegistration", main)
validate.bind("maxUnits", 6)
validate.bind("status", "VALIDATE")

check = Scope("checkPolicy", validate)  # No maxUnits here

# Test static resolution
print("\nSTATIC SCOPING TEST:")
val, chain = resolve_static("maxUnits", check)
print(f"  Resolving 'maxUnits' in checkPolicy")
print(f"  Value: {val}")
print(f"  Chain searched: {' → '.join(chain)}")

# Test dynamic resolution
call_chain = [
    {"name": "main", "bindings": {"maxUnits": 8, "status": "GLOBAL"}},
    {"name": "validateRegistration", "bindings": {"maxUnits": 6, "status": "VALIDATE"}},
    {"name": "checkPolicy", "bindings": {}}
]

print("\nDYNAMIC SCOPING TEST:")
val, chain = resolve_dynamic("maxUnits", call_chain)
print(f"  Resolving 'maxUnits' in checkPolicy")
print(f"  Value: {val}")
print(f"  Chain searched: {' → '.join(chain)}")

print("\nCOMPARISON:")
print("  Static scoping: Follows lexical structure (code)")
print("  Dynamic scoping: Follows runtime call stack (execution)")
print("="*60)
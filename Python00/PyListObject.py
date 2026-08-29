# -*- coding: utf-8 -*-
"""
PyListObject.py -- Main runner for the Python memory model tutorial.

This script demonstrates Python's object identity, reference counting,
list references, string immutability, aliasing, shallow/deep copying,
and nested list mutation through 7 OOP demo classes organized into
the `pylistobject` package.

ARCHITECTURE:
    PyListObject.py  (this file -- main entry point)
    └-- pylistobject/
        ├-- __init__.py
        ├-- object_identity.py       -> ObjectIdentityDemo
        ├-- reference_counting.py    -> ReferenceCountingDemo
        ├-- list_references.py       -> ListReferenceDemo
        ├-- string_immutability.py   -> StringImmutabilityDemo
        ├-- list_aliasing.py         -> ListAliasingDemo
        ├-- shallow_vs_deep_copy.py  -> ShallowVsDeepCopyDemo
        └-- nested_list_mutation.py  -> NestedListMutationDemo

CONCEPTS COVERED:
    1. Object Identity (id())
       - Every Python object has a unique id (memory address in CPython).
       - Immutable types (int, str) get new ids on "modification" (rebinding).

    2. Reference Counting (sys.getrefcount())
       - CPython tracks how many names/containers reference each object.
       - getrefcount() returns actual_count + 1 (the argument is a reference).

    3. List References & Slicing
       - Slicing creates a new outer list with shared inner references.
       - Rebinding a slice element ≠ mutating the original.

    4. String Immutability
       - Strings can't be modified in place.
       - str[:] may reuse the same object (CPython optimization).

    5. List Aliasing & Copying
       - `=` creates an alias; `[:]`, `list()`, `.copy()` create shallow copies.
       - `+` concatenation creates a new list; `.append()` is in-place.

    6. Shallow vs Deep Copy
       - `list * N` duplicates references, not objects.
       - Mutation of shared inner lists propagates; rebinding does not.

    7. Nested List Mutation
       - 2D slicing shares inner lists.
       - Mixed-type lists with iteration demonstrate mutation vs rebinding.

NO DECORATORS are used anywhere in this project.

Run:
    python PyListObject.py
"""

# ------------------------------------------------------------------
# Imports -- all 7 demo classes from the pylistobject package
# ------------------------------------------------------------------
from pylistobject import (
    ObjectIdentityDemo,
    ReferenceCountingDemo,
    ListReferenceDemo,
    StringImmutabilityDemo,
    ListAliasingDemo,
    ShallowVsDeepCopyDemo,
    NestedListMutationDemo,
)


class PyListObject:
    """
    Main orchestrator class that instantiates all demo classes and
    runs their demonstrations in a logical sequence.

    This class serves as the single entry point for the entire tutorial.
    Each concept builds upon the previous one:
      1. Object identity -> foundation for understanding everything else
      2. Reference counting -> how Python tracks object lifetimes
      3. List references -> how slicing creates shared refs
      4. String immutability -> contrast with mutable lists
      5. List aliasing -> alias vs copy vs concat vs append
      6. Shallow vs deep copy -> pitfalls with nested structures
      7. Nested list mutation -> advanced scenarios combining all concepts
    """

    def __init__(self):
        """
        Initialize all 7 demo class instances.

        Each demo class encapsulates a specific concept with:
          - Detailed docstrings explaining the concept
          - Multiple methods demonstrating different aspects
          - A run_all() method that executes all demos in order
          - References to the original notebook code cells
        """
        # Instantiate each demo class.
        # Each class manages its own state and output formatting.
        self.object_identity_demo = ObjectIdentityDemo()
        self.reference_counting_demo = ReferenceCountingDemo()
        self.list_reference_demo = ListReferenceDemo()
        self.string_immutability_demo = StringImmutabilityDemo()
        self.list_aliasing_demo = ListAliasingDemo()
        self.shallow_vs_deep_copy_demo = ShallowVsDeepCopyDemo()
        self.nested_list_mutation_demo = NestedListMutationDemo()

    def run_all_demos(self):
        """
        Execute all 7 demonstrations in conceptual order.

        The order is intentional -- each concept builds on the previous:
          1. id() -> what it means for two names to share identity
          2. refcount -> how Python tracks those shared references
          3. list slicing -> shallow copies and shared elements
          4. string immutability -> why immutable types are "safe" to share
          5. aliasing -> the spectrum from alias to independent copy
          6. shallow vs deep copy -> when sharing is dangerous
          7. nested mutation -> putting it all together
        """
        # Print a banner at the start
        print("+" + "=" * 58 + "+")
        print("|   Python Memory Model & List Object Tutorial (OOP)      |")
        print("|   No decorators - Pure classes - Modular design          |")
        print("+" + "=" * 58 + "+")

        # Run each demo class in sequence
        self.object_identity_demo.run_all()
        self.reference_counting_demo.run_all()
        self.list_reference_demo.run_all()
        self.string_immutability_demo.run_all()
        self.list_aliasing_demo.run_all()
        self.shallow_vs_deep_copy_demo.run_all()
        self.nested_list_mutation_demo.run_all()

        # Print a closing summary
        print(f"\n{'='*60}")
        print("  [OK] All 7 demonstrations completed successfully.")
        print(f"{'='*60}")
        print("\n  Concepts covered:")
        print("    1. Object Identity (id)")
        print("    2. Reference Counting (sys.getrefcount)")
        print("    3. List References & Slicing")
        print("    4. String Immutability")
        print("    5. List Aliasing & Copying")
        print("    6. Shallow vs Deep Copy")
        print("    7. Nested List Mutation")
        print("\n  Key rules to remember:")
        print("    - Assignment (=) creates an ALIAS, not a copy.")
        print("    - Slicing ([:]) creates a SHALLOW copy.")
        print("    - Immutable objects (int, str) are rebound, not mutated.")
        print("    - Mutable objects (list, dict) can be mutated IN PLACE.")
        print("    - Mutation propagates through shared references.")
        print("    - Rebinding only affects the specific name/slot.")


# ------------------------------------------------------------------
# Entry point
# ------------------------------------------------------------------
if __name__ == "__main__":
    # Create the main orchestrator and run everything
    tutorial = PyListObject()
    tutorial.run_all_demos()
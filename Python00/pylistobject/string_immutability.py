# -*- coding: utf-8 -*-
"""
string_immutability.py -- Demonstrates string immutability and how it
contrasts with list mutability in Python.

CONCEPT: Strings in Python are immutable sequences. You cannot change a
character inside a string -- any "modification" actually creates a brand-
new string object. This has important implications for identity (id()):

  - Assigning s2 = s1 creates an alias (same id).
  - Reassigning s2 = "new value" creates a NEW object (different id).
  - s2 = s1[:] may return the SAME object in CPython (optimization),
    because since strings can't be mutated, sharing is always safe.

Compare with lists:
  - list2 = list1[:] ALWAYS creates a new list object.

NO DECORATORS are used in this module (per project convention).
"""


class StringImmutabilityDemo:
    """
    Demonstrates that strings are immutable in Python and contrasts
    their behavior with mutable lists.

    Key takeaways:
      1. str is immutable -- you can't do s[0] = 'X'.
      2. Reassignment creates a new object.
      3. str[:] may reuse the same object (CPython optimization).
      4. list[:] always creates a new object.
    """

    def __init__(self):
        self.section_title = "String Immutability Demo"

    # --------------------------------------------------------------
    # Demo 1: String rebinding
    # --------------------------------------------------------------
    def demonstrate_string_rebinding(self):
        """
        Shows that assigning stringzy = stringy creates an alias,
        but reassigning stringzy to a new literal produces a new object.

        ORIGINAL NOTEBOOK CODE (cell 4):
            stringy = input("Enter a string:")
            stringzy = stringy
            stringzy = "I am a different string object"

        NOTE: Hardcoded values used instead of input().
        """
        print("\n--- 4a. String Rebinding ---")

        # Step 1: Create a string object.
        stringy: str = "Hello, Python!"
        print(f"  stringy = '{stringy}'")
        print(f"  id(stringy) = {id(stringy)}")

        # Step 2: stringzy = stringy -> alias (same object, same id).
        # No copy is made. Both names point to the same str object.
        stringzy: str = stringy
        print(f"\n  stringzy = stringy  (alias)")
        print(f"  id(stringy)  = {id(stringy)}")
        print(f"  id(stringzy) = {id(stringzy)}")
        print(f"  Same object? {stringy is stringzy}")  # True

        # Step 3: Reassign stringzy to a new string literal.
        # A brand-new str object is created. stringy is unaffected.
        stringzy = "I am a different string object"
        print(f"\n  stringzy = 'I am a different string object'  (rebinding)")
        print(f"  id(stringzy) = {id(stringzy)}  (NEW object)")
        print(f"  stringy  = '{stringy}'   (unchanged)")
        print(f"  stringzy = '{stringzy}'")

    # --------------------------------------------------------------
    # Demo 2: String slice [:] identity
    # --------------------------------------------------------------
    def demonstrate_string_slice_identity(self):
        """
        For immutable types like str, Python's CPython implementation
        may optimize full-slice ([:]) to return the same object, since
        there's no risk of unintended mutation through a shared reference.

        Contrast: list[:] ALWAYS creates a new list because lists are
        mutable -- sharing would be dangerous.

        ORIGINAL NOTEBOOK CODE (cell 5):
            stringzy = stringy[:]
        """
        print("\n--- 4b. String Slice [:] vs List Slice [:] ---")

        # String case: str[:] may return the same object
        stringy: str = "Hello, Python!"
        stringzy: str = stringy[:]

        print(f"  stringy  = '{stringy}'")
        print(f"  stringzy = stringy[:]")
        print(f"  id(stringy)  = {id(stringy)}")
        print(f"  id(stringzy) = {id(stringzy)}")
        print(f"  Same object? {stringy is stringzy}")
        print("  -> CPython may reuse the same object for immutable str[:]")

        # List case: list[:] ALWAYS creates a new object
        list_a = [1, 2, 3]
        list_b = list_a[:]
        print(f"\n  Contrast with lists:")
        print(f"  list_a = {list_a}")
        print(f"  list_b = list_a[:]")
        print(f"  id(list_a) = {id(list_a)}")
        print(f"  id(list_b) = {id(list_b)}")
        print(f"  Same object? {list_a is list_b}")  # Always False
        print("  -> list[:] ALWAYS creates a new list (mutable = must copy)")

        # After rebinding stringzy, it gets a new id
        stringzy = "I am a different string object"
        print(f"\n  After stringzy = 'I am a different string object':")
        print(f"  id(stringzy) = {id(stringzy)}  (new object)")
        print(f"  stringy  = '{stringy}'")
        print(f"  stringzy = '{stringzy}'")

    # --------------------------------------------------------------
    # Runner
    # --------------------------------------------------------------
    def run_all(self):
        """Execute all demonstrations in this class."""
        print(f"\n{'='*60}")
        print(f"  {self.section_title}")
        print(f"{'='*60}")
        self.demonstrate_string_rebinding()
        self.demonstrate_string_slice_identity()

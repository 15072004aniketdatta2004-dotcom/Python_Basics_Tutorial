# -*- coding: utf-8 -*-
"""
object_identity.py -- Demonstrates Python's object identity model using id().

CONCEPT: Every Python object lives at a memory address. The built-in id()
function returns a unique integer identifier for that object (in CPython,
this is literally the memory address). Two names that refer to the SAME
object will have the SAME id(). When an immutable object (int, str, tuple)
is "modified", Python actually creates a NEW object -- the original is
untouched and the name is simply rebound to the new object.

NO DECORATORS are used in this module (per project convention).
"""

import sys


class ObjectIdentityDemo:
    """
    Demonstrates how Python's id() function reveals whether two names
    point to the same underlying object or to different ones.

    Key takeaways taught by this class:
      1. Assignment (=) does NOT copy -- it creates an alias.
      2. Operations on immutable types (int, str) produce NEW objects.
      3. id() is the tool to verify shared vs. separate identity.
    """

    def __init__(self):
        # Section title used for console output formatting
        self.section_title = "Object Identity (id) Demo"

    # --------------------------------------------------------------
    # Demo 1: Integer identity and rebinding
    # --------------------------------------------------------------
    def demonstrate_int_identity(self):
        """
        Shows that integers are immutable. When we do `number += 1`,
        Python does NOT modify the existing int object in-place.
        Instead it creates a brand-new int object with value 3 and
        rebinds the name `number` to it. The old int(2) still exists
        (and `other_number` still points to it).

        ORIGINAL NOTEBOOK CODE (cell 1):
            number: int = 2
            other_number = number
            number += 1
            ... prints of id() and sys.getrefcount() ...
        """
        print("\n--- 1a. Integer Identity & Rebinding ---")

        # Step 1: Create an integer object with value 2.
        # `number` is a NAME (label) that points to the int object 2.
        number: int = 2
        print(f"  number = {number}")
        print(f"  id(number) = {id(number)}")

        # Step 2: `other_number = number` makes other_number point to
        # the SAME int(2) object. No copy is made.
        other_number = number
        print(f"\n  other_number = number  (alias -- no copy)")
        print(f"  id(other_number) = {id(other_number)}")
        print(f"  Same object? {id(number) == id(other_number)}")  # True

        # Step 3: `number += 1` is equivalent to `number = number + 1`.
        # Since int is IMMUTABLE, Python:
        #   (a) computes 2 + 1 = 3 -> creates a NEW int object with value 3
        #   (b) rebinds the name `number` to this new int(3)
        # `other_number` is unaffected -- it still points to int(2).
        number += 1  # NOT in-place; creates a new object
        print(f"\n  After number += 1:")
        print(f"  number       = {number}")
        print(f"  other_number = {other_number}")
        print(f"  id(number)       = {id(number)}")
        print(f"  id(other_number) = {id(other_number)}")
        print(f"  Same object? {id(number) == id(other_number)}")  # False

        # Step 4: Reference counts.
        # sys.getrefcount(obj) always returns actual_count + 1 because
        # passing the object as an argument to getrefcount() itself
        # creates a temporary reference.
        print(f"\n  sys.getrefcount(number)       = {sys.getrefcount(number)}")
        print(f"  sys.getrefcount(other_number) = {sys.getrefcount(other_number)}")
        print("  (These counts are +1 because the argument itself is a reference)")

    # --------------------------------------------------------------
    # Demo 2: String identity -- assignment vs rebinding
    # --------------------------------------------------------------
    def demonstrate_string_identity(self):
        """
        Shows that strings behave like integers (immutable).
        Assigning stringzy = stringy creates an alias; reassigning
        stringzy to a new literal creates a new object.

        ORIGINAL NOTEBOOK CODE (cells 4 & 5):
            stringy = input("Enter a string:")
            stringzy = stringy
            stringzy = "I am a different string object"
            ... and the [:] slice variant ...

        NOTE: We use hardcoded values instead of input() so the
        tutorial is runnable non-interactively.
        """
        print("\n--- 1b. String Identity & Rebinding ---")

        # Using a hardcoded value (original used input())
        stringy: str = "Hello, Python!"
        print(f"  stringy = '{stringy}'")

        # stringzy = stringy -> alias, same object
        stringzy: str = stringy
        print(f"  stringzy = stringy")
        print(f"  id(stringy)  = {id(stringy)}")
        print(f"  id(stringzy) = {id(stringzy)}")
        print(f"  Same object? {id(stringy) == id(stringzy)}")  # True

        # Rebinding stringzy to a new string literal
        stringzy = "I am a different string object"
        print(f"\n  After stringzy = 'I am a different string object':")
        print(f"  id(stringzy) = {id(stringzy)}  (new object!)")
        print(f"  stringy  = '{stringy}'   (unchanged)")
        print(f"  stringzy = '{stringzy}'")

    # --------------------------------------------------------------
    # Demo 3: String slicing with [:]
    # --------------------------------------------------------------
    def demonstrate_string_slice_identity(self):
        """
        For IMMUTABLE types, Python may optimize str[:] to return the
        SAME object (since it can never be mutated, there is no risk).
        This is an implementation detail of CPython -- do not rely on it.

        ORIGINAL NOTEBOOK CODE (cell 5):
            stringzy = stringy[:]
        """
        print("\n--- 1c. String Slice [:] Identity ---")

        stringy: str = "Hello, Python!"
        stringzy: str = stringy[:]  # Slice of entire string

        print(f"  stringy    = '{stringy}'")
        print(f"  stringzy   = stringy[:]")
        print(f"  id(stringy)  = {id(stringy)}")
        print(f"  id(stringzy) = {id(stringzy)}")
        # In CPython, these are often the SAME id for str[:] because
        # the runtime knows strings are immutable and can safely reuse
        # the object. Compare this with list[:] which ALWAYS creates
        # a new list (because lists are mutable).
        print(f"  Same object? {id(stringy) == id(stringzy)}")
        print("  (CPython optimizes str[:] to reuse the same object)")

    # --------------------------------------------------------------
    # Runner
    # --------------------------------------------------------------
    def run_all(self):
        """Execute all demonstrations in this class."""
        print(f"\n{'='*60}")
        print(f"  {self.section_title}")
        print(f"{'='*60}")
        self.demonstrate_int_identity()
        self.demonstrate_string_identity()
        self.demonstrate_string_slice_identity()

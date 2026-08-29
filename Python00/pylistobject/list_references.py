# -*- coding: utf-8 -*-
"""
list_references.py -- Demonstrates how list slicing and copying work
with respect to object identity.

CONCEPT: When you slice a list (e.g., alist[2:4]), Python creates a
NEW list object (new outer container), but the ELEMENTS inside the new
list are references to the SAME objects as in the original. This is
called a "shallow copy". Mutating the slice's element (rebinding) does
NOT affect the original list, because rebinding only changes what the
slice's slot points to -- the original slot is untouched.

NO DECORATORS are used in this module (per project convention).
"""


class ListReferenceDemo:
    """
    Demonstrates list slicing, shallow copying via [:], and the
    distinction between REBINDING an element vs. MUTATING an object.

    Key takeaways:
      1. Slicing creates a new outer list but shares inner references.
      2. Rebinding a slice element (aslice[0] = 'x') does NOT affect
         the original list -- it only changes what aslice[0] points to.
      3. list[:] is equivalent to list.copy() -- a shallow copy.
    """

    def __init__(self):
        self.section_title = "List References & Slicing Demo"

    # --------------------------------------------------------------
    # Demo 1: Slice creates shared references
    # --------------------------------------------------------------
    def demonstrate_slice_identity(self):
        """
        Creates a list and a slice of it. Verifies that:
          - The slice is a NEW list object (different id from original).
          - The elements INSIDE the slice share id() with the originals.
          - Rebinding a slice element does NOT propagate to the original.

        ORIGINAL NOTEBOOK CODE (cell 2):
            alist = ['a','b','c','d','e','f']
            aslice = alist[2:4]
            ... id comparisons ...
            aslice[0] = 'x'
        """
        print("\n--- 3a. Slice Creates Shared References ---")

        # Create a list of single-character strings.
        # (NOTE: The type hint says list[int] in the original code,
        #  but the values are actually strings. We keep them as strings.)
        alist: list[str] = ['a', 'b', 'c', 'd', 'e', 'f']
        print(f"  alist = {alist}")
        print(f"  id(alist) = {id(alist)}")

        # Slicing alist[2:4] creates a NEW list containing references
        # to the objects at indices 2 and 3 of alist.
        # The new list is a separate container, but 'c' and 'd' are
        # the same string objects (shared references).
        aslice: list[str] = alist[2:4]
        print(f"\n  aslice = alist[2:4] = {aslice}")
        print(f"  id(aslice) = {id(aslice)}  (different from alist!)")

        # Verify shared references: alist[2] and aslice[0] point to
        # the same 'c' string object.
        print(f"\n  id(alist[2])  = {id(alist[2])}")
        print(f"  id(aslice[0]) = {id(aslice[0])}")
        print(f"  alist[2] is aslice[0]? {alist[2] is aslice[0]}")  # True

        print(f"  id(alist[3])  = {id(alist[3])}")
        print(f"  id(aslice[1]) = {id(aslice[1])}")
        print(f"  alist[3] is aslice[1]? {alist[3] is aslice[1]}")  # True

        # Rebinding: aslice[0] = 'x'
        # This makes aslice[0] point to a NEW string object 'x'.
        # alist[2] is NOT affected because we only changed the slice's
        # internal pointer -- we did not mutate the original 'c' object.
        aslice[0] = 'x'
        print(f"\n  After aslice[0] = 'x':")
        print(f"  alist  = {alist}   (unchanged -- alist[2] is still 'c')")
        print(f"  aslice = {aslice}          (aslice[0] rebound to 'x')")
        print(f"  id(alist[2])  = {id(alist[2])}  (still 'c')")
        print(f"  id(aslice[0]) = {id(aslice[0])}  (new 'x' object)")

    # --------------------------------------------------------------
    # Demo 2: Shallow copy via [:]
    # --------------------------------------------------------------
    def demonstrate_shallow_copy_via_slice(self):
        """
        Using list[:] (full slice) creates a shallow copy -- a brand-new
        list object whose elements reference the same objects as the
        original. Rebinding an element in the copy does not affect the
        original, and vice versa.

        ORIGINAL NOTEBOOK CODE (cell 3):
            n = int(input(...))
            a = [int(input(...)) for _ in range(0,n)]
            b = a[:]
            b[0] = 1

        NOTE: We use hardcoded values instead of input().
        """
        print("\n--- 3b. Shallow Copy via [:] ---")

        # Hardcoded list (original used input())
        a = [10, 20, 30, 40, 50]
        print(f"  a = {a}")
        print(f"  id(a) = {id(a)}")

        # b = a[:] creates a SHALLOW COPY:
        # - b is a NEW list object (different id from a)
        # - b[0], b[1], ... reference the same int objects as a[0], a[1], ...
        b = a[:]
        print(f"\n  b = a[:] (shallow copy)")
        print(f"  id(b) = {id(b)}  (different from a)")
        print(f"  a is b? {a is b}")  # False

        # Rebinding b[0] only changes where b's first slot points.
        # a[0] remains 10.
        b[0] = 1
        print(f"\n  After b[0] = 1:")
        print(f"  a = {a}  (unchanged)")
        print(f"  b = {b}")
        print(f"  id(a) = {id(a)}")
        print(f"  id(b) = {id(b)}")

    # --------------------------------------------------------------
    # Runner
    # --------------------------------------------------------------
    def run_all(self):
        """Execute all demonstrations in this class."""
        print(f"\n{'='*60}")
        print(f"  {self.section_title}")
        print(f"{'='*60}")
        self.demonstrate_slice_identity()
        self.demonstrate_shallow_copy_via_slice()

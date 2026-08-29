# -*- coding: utf-8 -*-
"""
reference_counting.py -- Demonstrates Python's reference counting mechanism.

CONCEPT: CPython uses reference counting as its primary memory management
strategy. Every object has an internal counter that tracks how many names,
containers, or other objects refer to it. When the reference count drops
to zero, the object is immediately deallocated.

sys.getrefcount(obj) returns the current reference count of `obj`, but it
always shows one MORE than the "true" count because passing `obj` as an
argument to the function temporarily creates an additional reference.

NO DECORATORS are used in this module (per project convention).
"""

import sys


class ReferenceCountingDemo:
    """
    Demonstrates sys.getrefcount() and how assignments, container
    membership, and aliasing affect reference counts.

    Key takeaways:
      1. sys.getrefcount() always returns actual_count + 1.
      2. Assigning x[0] = x[2] makes x[0] and x[2] point to the
         same object, increasing that object's refcount.
      3. Small integers (-5 to 256) are cached (interned) by CPython,
         so their refcounts are artificially high.
    """

    def __init__(self):
        self.section_title = "Reference Counting (sys.getrefcount) Demo"

    # --------------------------------------------------------------
    # Demo 1: Basic integer reference counting
    # --------------------------------------------------------------
    def demonstrate_int_refcount(self):
        """
        Shows how creating aliases increases the reference count of
        an integer object, and how += on an immutable type shifts the
        reference to a different object entirely.

        ORIGINAL NOTEBOOK CODE (cell 1, last two lines):
            print(sys.getrefcount(number))
            print(sys.getrefcount(other_number))
        """
        print("\n--- 2a. Integer Reference Counting ---")

        number: int = 2
        other_number = number  # Both point to int(2)

        # At this point int(2) has at least:
        #   - 1 reference from `number`
        #   - 1 reference from `other_number`
        #   - many internal CPython references (small int cache)
        #   - +1 from passing it to getrefcount()
        print(f"  number = {number}, other_number = {other_number}")
        print(f"  sys.getrefcount(number)       = {sys.getrefcount(number)}")
        print(f"  sys.getrefcount(other_number) = {sys.getrefcount(other_number)}")
        print("  (Both refer to the same int(2) object -- counts should match)")

        # After rebinding `number` to a new int(3):
        number += 1
        print(f"\n  After number += 1:")
        print(f"  number = {number}, other_number = {other_number}")
        print(f"  sys.getrefcount(number)       = {sys.getrefcount(number)}")
        print(f"  sys.getrefcount(other_number) = {sys.getrefcount(other_number)}")
        print("  (number now points to int(3), other_number still to int(2))")

    # --------------------------------------------------------------
    # Demo 2: Nested list reference counting
    # --------------------------------------------------------------
    def demonstrate_nested_list_refcount(self):
        """
        Creates a list of sublists and then makes some elements share
        the same sublist object via assignment. Shows how this changes
        reference counts.

        ORIGINAL NOTEBOOK CODE (cell 11):
            x = [[22],[33],[22],[33]]
            x[0] = x[2]
            x[1] = x[3]
            ... prints of id() and sys.getrefcount() ...

        KEY INSIGHT: After x[0] = x[2], both x[0] and x[2] point to
        the SAME inner list object [22]. The original [22] that was at
        x[0] loses a reference and may be garbage collected.
        """
        print("\n--- 2b. Nested List Reference Counting ---")

        # Step 1: Create a list with 4 inner lists.
        # IMPORTANT: Each [22] and [33] literal creates a SEPARATE
        # list object, even though they contain the same values.
        x = [[22], [33], [22], [33]]
        print(f"  x = {x}")
        print(f"  id(x) = {id(x)}")
        print(f"  id(x[0]) = {id(x[0])}, id(x[2]) = {id(x[2])}")
        print(f"  x[0] is x[2]? {x[0] is x[2]}")  # False -- separate objects
        print(f"  sys.getrefcount(x) = {sys.getrefcount(x)}")

        # Step 2: Make x[0] point to the same object as x[2].
        # The old list at x[0] loses a reference.
        x[0] = x[2]
        # Make x[1] point to the same object as x[3].
        x[1] = x[3]

        print(f"\n  After x[0] = x[2] and x[1] = x[3]:")
        print(f"  id(x[0]) = {id(x[0])}")
        print(f"  id(x[1]) = {id(x[1])}")
        print(f"  id(x[2]) = {id(x[2])}  (same as x[0])")
        print(f"  id(x[3]) = {id(x[3])}  (same as x[1])")
        print(f"  x[0] is x[2]? {x[0] is x[2]}")  # True
        print(f"  x[1] is x[3]? {x[1] is x[3]}")  # True

        # Reference counts:
        # sys.getrefcount(x) = 2 -> x itself + the getrefcount argument
        # sys.getrefcount(x[0]) = 3 -> x[0], x[2], and the argument
        # sys.getrefcount(x[1]) = 3 -> x[1], x[3], and the argument
        print(f"\n  sys.getrefcount(x)    = {sys.getrefcount(x)}     (x + arg = 2)")
        print(f"  sys.getrefcount(x[0]) = {sys.getrefcount(x[0])}  (x[0] + x[2] + arg = 3)")
        print(f"  sys.getrefcount(x[1]) = {sys.getrefcount(x[1])}  (x[1] + x[3] + arg = 3)")
        print(f"  sys.getrefcount(x[2]) = {sys.getrefcount(x[2])}  (same object as x[0])")
        print(f"  sys.getrefcount(x[3]) = {sys.getrefcount(x[3])}  (same object as x[1])")

    # --------------------------------------------------------------
    # Runner
    # --------------------------------------------------------------
    def run_all(self):
        """Execute all demonstrations in this class."""
        print(f"\n{'='*60}")
        print(f"  {self.section_title}")
        print(f"{'='*60}")
        self.demonstrate_int_refcount()
        self.demonstrate_nested_list_refcount()

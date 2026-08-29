# -*- coding: utf-8 -*-
"""
nested_list_mutation.py -- Demonstrates how slicing and mutation interact
with nested (2D) lists, and how mixed-type lists with iteration behave.

CONCEPT: When you slice a 2D list (b = a[1:]), the outer list is new,
but the inner lists are SHARED. This means:

  - Mutating an inner list via `a[1][0] = 100` is visible through `b[0]`
    (because a[1] and b[0] are the same inner list object).
  - REBINDING a slot via `b[0] = [10, 11]` breaks the shared reference
    for that specific slot only.

The last demo shows a complex scenario with mixed types, iteration, and
in-place mutation tracking.

NO DECORATORS are used in this module (per project convention).
"""


class NestedListMutationDemo:
    """
    Demonstrates mutation and rebinding in nested (2D) lists and
    complex mixed-type list structures.

    Key takeaways:
      1. Slicing a 2D list -> new outer list, shared inner lists.
      2. Inner list mutation propagates through shared references.
      3. Rebinding a slot breaks that specific shared reference.
      4. Integer math (c[2] = c[2] + 1) is rebinding (new int object).
    """

    def __init__(self):
        self.section_title = "Nested List Mutation Demo"

    # --------------------------------------------------------------
    # Demo 1: 2D list slice and mutation
    # --------------------------------------------------------------
    def demonstrate_2d_slice_mutation(self):
        """
        Slicing a 2D list:
          b = a[1:]  -> b is a new outer list, but b[0] IS a[1],
          and b[1] IS a[2] (shared inner lists).

        Then we demonstrate three kinds of operations:
          1. a[1][0] = 100 -> inner mutation (visible through b[0])
          2. b[0] = [10, 11] -> rebinding (breaks shared ref for b[0])
          3. b[1][0] = 99 -> inner mutation again (visible through a[2])

        ORIGINAL NOTEBOOK CODE (cell 15):
            a = [[1,2,3],[4,5,6],[7,8,9]]
            b = a[1:]
            a[1][0] = 100
            b[0] = [10, 11]
            b[1][0] = 99
        """
        print("\n--- 7a. 2D List Slice and Mutation ---")

        a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        print(f"  a = {a}")

        # b = a[1:] creates a new outer list containing references
        # to a[1] and a[2]. At this point:
        #   b[0] IS a[1]  (same [4,5,6] object)
        #   b[1] IS a[2]  (same [7,8,9] object)
        b = a[1:]
        print(f"  b = a[1:] = {b}")
        print(f"  b[0] is a[1]? {b[0] is a[1]}")  # True
        print(f"  b[1] is a[2]? {b[1] is a[2]}")  # True

        # OPERATION 1: Inner mutation through a[1].
        # Since b[0] IS a[1], this change is visible through b[0].
        a[1][0] = 100
        print(f"\n  After a[1][0] = 100  (inner mutation):")
        print(f"  a = {a}")
        print(f"  b = {b}  (b[0] reflects the change!)")

        # OPERATION 2: Rebinding b[0] to a completely new list.
        # This breaks the shared reference -- b[0] no longer IS a[1].
        b[0] = [10, 11]
        print(f"\n  After b[0] = [10, 11]  (rebinding -- breaks shared ref):")
        print(f"  a = {a}  (a[1] unchanged)")
        print(f"  b = {b}")
        print(f"  b[0] is a[1]? {b[0] is a[1]}")  # Now False

        # OPERATION 3: Inner mutation through b[1].
        # b[1] is still a[2], so this affects a[2].
        b[1][0] = 99
        print(f"\n  After b[1][0] = 99  (inner mutation through b[1]):")
        print(f"  a = {a}  (a[2][0] changed!)")
        print(f"  b = {b}")
        print(f"  b[1] is a[2]? {b[1] is a[2]}")  # Still True

        # Show identity details
        print(f"\n  Identity details:")
        print(f"  id(a[0]) = {id(a[0])}, id(a[1]) = {id(a[1])}, id(a[2]) = {id(a[2])}")
        print(f"  id(b[0]) = {id(b[0])}, id(b[1]) = {id(b[1])}")

    # --------------------------------------------------------------
    # Demo 2: Mixed-type list with iteration and mutation
    # --------------------------------------------------------------
    def demonstrate_mixed_type_iteration(self):
        """
        A complex scenario combining:
          - A list `a` of strings
          - A string `b` used as an iterable
          - A mixed-type list `c = [a, b, 5]`
          - A shallow copy `d = c[:]`
          - Iterating over d[1] (which is string b) and appending
            each character to list a, while incrementing c[2]

        KEY INSIGHTS:
          - c[0] IS a, and d[0] IS also a (shared references).
            Appending to `a` is visible through c[0] and d[0].
          - c[2] = c[2] + 1 is REBINDING (ints are immutable).
            d[2] still points to the old int value.
          - d[1] IS b (shared string reference), but strings are
            immutable so no mutation risk exists.

        ORIGINAL NOTEBOOK CODE (cell 16, second half):
            a = ['a','b','c']
            b = "2316"
            c = [a, b, 5]
            d = c[:]
            for x in d[1]:
                a.append(x)
                c[2] = c[2] + 1
        """
        print("\n--- 7b. Mixed-Type List with Iteration ---")

        # Setup
        a: list[str] = ['a', 'b', 'c']
        b: str = "2316"
        # c is a mixed-type list: [reference to list a, string b, int 5]
        c = [a, b, 5]
        # d is a shallow copy of c -- new outer list, shared inner refs
        d = c[:]

        print(f"  a = {a}")
        print(f"  b = '{b}'")
        print(f"  c = {c}")
        print(f"  d = c[:] = {d}")
        print(f"  c[0] is a? {c[0] is a}")  # True
        print(f"  d[0] is a? {d[0] is a}")  # True
        print(f"  c[1] is b? {c[1] is b}")  # True
        print(f"  d[1] is b? {d[1] is b}")  # True

        # Iteration: for each character x in d[1] (which is "2316"):
        #   1. a.append(x) -- IN-PLACE mutation of list a.
        #      Since c[0] and d[0] both reference a, this is visible
        #      through c[0] and d[0] too.
        #   2. c[2] = c[2] + 1 -- REBINDING. Since int is immutable,
        #      c[2] + 1 creates a new int object, and c[2] is rebound
        #      to it. d[2] is NOT affected (still points to the old int).
        print(f"\n  Iterating over d[1] = '{d[1]}':")
        for x in d[1]:
            a.append(x)
            c[2] = c[2] + 1
            print(f"    Appended '{x}' to a; c[2] incremented to {c[2]}")

        print(f"\n  After iteration:")
        print(f"  a = {a}  (characters appended)")
        print(f"  b = '{b}'  (immutable -- unchanged)")
        print(f"  c = {c}")
        print(f"  d = {d}")

        # Identity analysis
        print(f"\n  Identity analysis:")
        print(f"  id(a) = {id(a)}")
        print(f"  id(b) = {id(b)}")
        print(f"  id(c) = {id(c)}")
        print(f"  id(d) = {id(d)}")

        # c[2] was rebound 4 times (once per iteration).
        # d[2] still points to the original int(5).
        print(f"\n  c[2] = {c[2]}, d[2] = {d[2]}")
        print(f"  id(c[2]) = {id(c[2])}  (new int object after rebinding)")
        print(f"  id(d[2]) = {id(d[2])}  (still the original int(5))")
        print(f"  c[2] is d[2]? {c[2] is d[2]}")  # False

        # Demonstrate id(c[2] + 1) -- this creates yet another temp object
        print(f"\n  id(c[2] + 1) = {id(c[2] + 1)}")
        print("  (This is a brand-new int object, created by the + operation)")

    # --------------------------------------------------------------
    # Runner
    # --------------------------------------------------------------
    def run_all(self):
        """Execute all demonstrations in this class."""
        print(f"\n{'='*60}")
        print(f"  {self.section_title}")
        print(f"{'='*60}")
        self.demonstrate_2d_slice_mutation()
        self.demonstrate_mixed_type_iteration()

# -*- coding: utf-8 -*-
"""
list_aliasing.py -- Demonstrates the difference between aliasing,
shallow copying, concatenation, and the list() constructor.

CONCEPT: Python names are labels attached to objects, not boxes that
contain values. Understanding this distinction is critical:

  - ALIAS (l2 = l1): l2 and l1 are two names for the SAME object.
    Any in-place mutation via l1 is visible through l2, and vice versa.

  - SHALLOW COPY (l2 = l1[:] or l2 = list(l1)): l2 is a NEW list
    object, but its elements reference the SAME inner objects as l1.

  - CONCATENATION (l3 = l1 + [4]): Creates a NEW list. The original
    l1 is unmodified.

  - IN-PLACE MUTATION (l1.append(5)): Modifies l1 in place. All
    aliases see the change.

NO DECORATORS are used in this module (per project convention).
"""


class ListAliasingDemo:
    """
    Demonstrates how aliasing, shallow copying, concatenation, and
    in-place operations differ in their effect on list identity.

    Key takeaways:
      1. l2 = l1 -> alias (same object).
      2. l3 = [l1, l1, l1] -> three references to the SAME list;
         mutating l1 is visible through all of l3.
      3. l3 = [l1[:], l1[:], l1[:]] -> three INDEPENDENT copies.
      4. l3 = l1 + [4] -> concatenation creates a NEW list.
      5. l1.append(5) -> in-place; visible through alias l2.
      6. list(l1) and l1[:] both create shallow copies.
    """

    def __init__(self):
        self.section_title = "List Aliasing & Copying Demo"

    # --------------------------------------------------------------
    # Demo 1: Alias vs reference copies in nested lists
    # --------------------------------------------------------------
    def demonstrate_alias_vs_copy(self):
        """
        Shows the difference between:
          - [l1, l1, l1]   -> all three elements are the SAME object
          - [l1[:], l1[:]] -> each element is an independent shallow copy

        ORIGINAL NOTEBOOK CODE (cells 6 & 7):
            l1 = [1,2,3]; l2 = l1; l3 = [l1,l1,l1]; l1[0] = 5
            l1 = [1,2,3]; l2 = l1; l3 = [l1[:],l1[:],l1[:]]; l1[0] = 5
        """
        print("\n--- 5a. Alias: [l1, l1, l1] (shared references) ---")

        # CASE 1: l3 contains three references to the SAME list object l1
        l1 = [1, 2, 3]
        l2 = l1  # l2 is an alias for l1
        l3 = [l1, l1, l1]  # All three slots point to l1

        # Mutating l1 is visible through every slot of l3,
        # because they all point to the same object.
        l1[0] = 5
        print(f"  l1 = {l1}")
        print(f"  l3[0] = {l3[0]}  (same as l1)")
        print(f"  l3[1] = {l3[1]}  (same as l1)")
        print(f"  l3[2] = {l3[2]}  (same as l1)")
        print(f"  id(l1) = {id(l1)}")
        print(f"  id(l2) = {id(l2)}  (alias)")
        print(f"  id(l3[0]) = {id(l3[0])}")
        print(f"  id(l3[1]) = {id(l3[1])}")
        print(f"  id(l3[2]) = {id(l3[2])}")
        print(f"  All same? {id(l1) == id(l3[0]) == id(l3[1]) == id(l3[2])}")

        print("\n--- 5b. Copy: [l1[:], l1[:], l1[:]] (independent copies) ---")

        # CASE 2: l3 contains three SEPARATE shallow copies of l1
        l1 = [1, 2, 3]
        l2 = l1
        l3 = [l1[:], l1[:], l1[:]]  # Each [:] creates a new list

        # Mutating l1 does NOT affect l3's elements, because they are
        # independent copies.
        l1[0] = 5
        print(f"  l1 = {l1}")
        print(f"  l3[0] = {l3[0]}  (independent copy -- unaffected)")
        print(f"  l3[1] = {l3[1]}  (independent copy -- unaffected)")
        print(f"  l3[2] = {l3[2]}  (independent copy -- unaffected)")
        print(f"  id(l1)    = {id(l1)}")
        print(f"  id(l2)    = {id(l2)}  (alias of l1)")
        print(f"  id(l3[0]) = {id(l3[0])}  (different)")
        print(f"  id(l3[1]) = {id(l3[1])}  (different)")
        print(f"  id(l3[2]) = {id(l3[2])}  (different)")

    # --------------------------------------------------------------
    # Demo 2: Concatenation vs in-place append
    # --------------------------------------------------------------
    def demonstrate_concat_vs_append(self):
        """
        Shows that:
          - L1 + [4] creates a NEW list (concatenation is not in-place).
          - L1.append(5) modifies L1 in place; alias L2 sees the change.

        ORIGINAL NOTEBOOK CODE (cell 8):
            L1 = [1,2,3]; L2 = L1
            L3 = L1 + [4]    # new list
            L1.append(5)      # in-place
        """
        print("\n--- 5c. Concatenation (+) vs In-Place Append ---")

        L1 = [1, 2, 3]
        L2 = L1  # Alias -- L2 is L1

        # L1 + [4] creates a SEPARATE copy of L1's elements plus [4].
        # L1 and L2 are unaffected by this operation.
        # The new list L3 contains references to the ORIGINAL int objects
        # (since ints are immutable, sharing is safe).
        L3 = L1 + [4]

        # L1.append(5) modifies L1 IN PLACE.
        # Since L2 is an alias for L1, L2 also reflects the change.
        L1.append(5)

        print(f"  L1 = {L1}  (original + appended 5)")
        print(f"  L2 = {L2}  (alias of L1 -- also shows 5)")
        print(f"  L3 = {L3}     (separate copy via + -- no 5)")
        print(f"  id(L1) = {id(L1)}")
        print(f"  id(L2) = {id(L2)}  (same as L1 -- alias)")
        print(f"  id(L3) = {id(L3)}  (different -- concatenation made a new list)")

    # --------------------------------------------------------------
    # Demo 3: list() constructor vs [:] vs = assignment
    # --------------------------------------------------------------
    def demonstrate_list_constructor(self):
        """
        Compares three ways of "copying" a list:
          - C = A       -> alias (same object)
          - D = A[:]    -> shallow copy (new list, shared elements)
          - B = list(A) -> shallow copy (new list, shared elements)

        All three shallow-copy methods ([:], list(), .copy()) produce
        equivalent results: a new outer container with shared inner
        references.

        ORIGINAL NOTEBOOK CODE (cell 9):
            A = [1,2]; B = list(A); C = A; D = A[:]
            B[1] = 7
        """
        print("\n--- 5d. list() Constructor vs [:] vs = ---")

        A = [1, 2]
        print(f"  A = {A}, id(A) = {id(A)}")

        # list(A) -- calls the list constructor with A as the iterable.
        # Creates a NEW outer list; inner elements are shared references.
        B = list(A)
        print(f"  B = list(A), id(B) = {id(B)}  (new list)")

        # C = A -- alias, same object
        C = A
        print(f"  C = A,       id(C) = {id(C)}  (alias of A)")

        # D = A[:] -- shallow copy, same as list(A)
        D = A[:]
        print(f"  D = A[:],    id(D) = {id(D)}  (new list)")

        # Mutating B does NOT affect A, C, or D (B is a separate list)
        B[1] = 7
        print(f"\n  After B[1] = 7:")
        print(f"  A = {A}  (unchanged)")
        print(f"  B = {B}  (modified)")
        print(f"  C = {C}  (alias of A -- unchanged)")
        print(f"  D = {D}  (copy of A -- unchanged)")
        print(f"\n  id(A) = {id(A)}")
        print(f"  id(B) = {id(B)}")
        print(f"  id(C) = {id(C)}  (== id(A))")
        print(f"  id(D) = {id(D)}")

    # --------------------------------------------------------------
    # Runner
    # --------------------------------------------------------------
    def run_all(self):
        """Execute all demonstrations in this class."""
        print(f"\n{'='*60}")
        print(f"  {self.section_title}")
        print(f"{'='*60}")
        self.demonstrate_alias_vs_copy()
        self.demonstrate_concat_vs_append()
        self.demonstrate_list_constructor()

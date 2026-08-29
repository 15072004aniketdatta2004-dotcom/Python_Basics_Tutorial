# -*- coding: utf-8 -*-
"""
shallow_vs_deep_copy.py -- Demonstrates shallow copy pitfalls with
list multiplication, explicit shared references, and literal lists.

CONCEPT: "Shallow copy" means a new outer container is created, but the
elements inside still point to the original objects. This is safe for
immutable elements (int, str, tuple), but DANGEROUS for mutable elements
(list, dict, set) because mutating an inner object through one reference
is visible through all other references.

Three common ways to accidentally create shared inner references:
  1. list * N   -- repeats references to the SAME inner objects
  2. [a, b, a]  -- explicitly stores the same object multiple times
  3. a[1:]      -- outer is new, inner lists are shared

Contrast with literal construction:
  [[22], [33], [22], [33]] -- each inner list is a SEPARATE object,
  even if they contain the same values.

NO DECORATORS are used in this module (per project convention).
"""


class ShallowVsDeepCopyDemo:
    """
    Demonstrates shallow copy pitfalls and the difference between
    shared references and separate objects that happen to have equal
    values.

    Key takeaways:
      1. list * 2 duplicates references, not objects.
      2. Mutating a shared inner list propagates to all references.
      3. Rebinding (x[0] = [1]) breaks the shared reference.
      4. Literal [[22],[33]] creates separate objects per element.
    """

    def __init__(self):
        self.section_title = "Shallow vs Deep Copy Demo"

    # --------------------------------------------------------------
    # Demo 1: list * N shares inner references
    # --------------------------------------------------------------
    def demonstrate_multiply_shared_refs(self):
        """
        When you multiply a list of lists (x = x * 2), the result
        contains repeated REFERENCES to the same inner list objects.
        Mutating one inner list mutates them all.

        ORIGINAL NOTEBOOK CODE (cell 12):
            x = [[22],[33]]
            x = x * 2
            x[0][0] = 1   # affects x[2][0] too!
            x[0] = [1]    # rebinding -- breaks shared ref

        IMPORTANT DISTINCTION:
          - x[0][0] = 1  -> MUTATION of the inner list object.
            All references to that inner list see the change.
          - x[0] = [1]   -> REBINDING of x's slot 0 to a new list.
            Only x[0] is affected; x[2] still points to the old object.
        """
        print("\n--- 6a. list * N Shares Inner References ---")

        x = [[22], [33]]
        print(f"  x = {x}")
        print(f"  id(x[0]) = {id(x[0])}, id(x[1]) = {id(x[1])}")
        print(f"  id(x[0][0]) = {id(x[0][0])}, id(x[1][0]) = {id(x[1][0])}")

        # x = x * 2 creates a NEW outer list with 4 elements,
        # but elements 0&2 point to the SAME inner [22] list,
        # and elements 1&3 point to the SAME inner [33] list.
        x = x * 2
        print(f"\n  After x = x * 2:")
        print(f"  x = {x}")
        print(f"  id(x[0]) = {id(x[0])}, id(x[2]) = {id(x[2])}")
        print(f"  x[0] is x[2]? {x[0] is x[2]}")  # True -- same object!
        print(f"  id(x[1]) = {id(x[1])}, id(x[3]) = {id(x[3])}")
        print(f"  x[1] is x[3]? {x[1] is x[3]}")  # True -- same object!

        # MUTATION: x[0][0] = 1 modifies the inner list object itself.
        # Since x[0] and x[2] are the SAME object, both reflect the change.
        x[0][0] = 1
        print(f"\n  After x[0][0] = 1  (MUTATION -- propagates to x[2]):")
        print(f"  x = {x}")
        print(f"  x[0] is x[2]? {x[0] is x[2]}")  # Still True

        # REBINDING: x[0] = [1] creates a NEW list [1] and makes x[0]
        # point to it. x[2] still points to the old (now mutated) list.
        x[0] = [1]
        print(f"\n  After x[0] = [1]  (REBINDING -- breaks shared ref):")
        print(f"  x = {x}")
        print(f"  x[0] is x[2]? {x[0] is x[2]}")  # Now False!
        print(f"  id(x[0]) = {id(x[0])}")
        print(f"  id(x[2]) = {id(x[2])}  (different -- no longer shared)")

    # --------------------------------------------------------------
    # Demo 2: Explicit shared references via variables
    # --------------------------------------------------------------
    def demonstrate_explicit_shared_refs(self):
        """
        Building a list like [a, b, a, b] explicitly stores references
        to the same objects a and b. This is equivalent to what list * 2
        does internally.

        ORIGINAL NOTEBOOK CODE (cell 13):
            a = [22]; b = [33]
            x = [a, b, a, b]
        """
        print("\n--- 6b. Explicit Shared References [a, b, a, b] ---")

        a = [22]
        b = [33]
        print(f"  a = {a}, id(a) = {id(a)}")
        print(f"  b = {b}, id(b) = {id(b)}")

        # x[0] and x[2] both point to `a`; x[1] and x[3] both point to `b`.
        x = [a, b, a, b]
        print(f"\n  x = [a, b, a, b] = {x}")
        print(f"  id(x[0]) = {id(x[0])}, id(x[2]) = {id(x[2])}")
        print(f"  x[0] is x[2]? {x[0] is x[2]}")  # True
        print(f"  x[0] is a?    {x[0] is a}")      # True
        print(f"  id(x[1]) = {id(x[1])}, id(x[3]) = {id(x[3])}")
        print(f"  x[1] is x[3]? {x[1] is x[3]}")  # True
        print(f"  x[1] is b?    {x[1] is b}")      # True

        # Inner element identity -- the int 22 inside a is the same
        # object referenced by x[0][0] and x[2][0]
        print(f"\n  Inner element identity:")
        print(f"  id(x[0][0]) = {id(x[0][0])}")
        print(f"  id(x[2][0]) = {id(x[2][0])}")
        print(f"  x[0][0] is x[2][0]? {x[0][0] is x[2][0]}")  # True

    # --------------------------------------------------------------
    # Demo 3: Literal lists -- each is a separate object
    # --------------------------------------------------------------
    def demonstrate_literal_separate_objects(self):
        """
        When you write [[22],[33],[22],[33]] as a literal, Python
        creates a SEPARATE inner list for each element, even if
        they contain the same values.

        Contrast with [a, b, a, b] where a and b are reused.

        ORIGINAL NOTEBOOK CODE (cell 14):
            x = [[22],[33],[22],[33]]
            print(id(x[0]), id(x[1]), id(x[2]), id(x[3]))
        """
        print("\n--- 6c. Literal Lists -- Each Is Separate ---")

        x = [[22], [33], [22], [33]]
        print(f"  x = {x}")
        print(f"  id(x[0]) = {id(x[0])}, id(x[2]) = {id(x[2])}")
        print(f"  x[0] is x[2]? {x[0] is x[2]}")  # False -- separate objects!

        # Even though x[0] == x[2] (equal values), they are NOT the
        # same object. Each [22] literal creates a new list.
        print(f"  x[0] == x[2]? {x[0] == x[2]}")  # True (equal values)
        print(f"  x[0] is x[2]? {x[0] is x[2]}")  # False (different objects)

        # However, the INT 22 inside them MAY share identity, because
        # CPython caches small integers (-5 to 256).
        print(f"\n  Inner int identity (CPython small-int cache):")
        print(f"  id(x[0][0]) = {id(x[0][0])}")
        print(f"  id(x[2][0]) = {id(x[2][0])}")
        print(f"  x[0][0] is x[2][0]? {x[0][0] is x[2][0]}")  # True (cached)

    # --------------------------------------------------------------
    # Runner
    # --------------------------------------------------------------
    def run_all(self):
        """Execute all demonstrations in this class."""
        print(f"\n{'='*60}")
        print(f"  {self.section_title}")
        print(f"{'='*60}")
        self.demonstrate_multiply_shared_refs()
        self.demonstrate_explicit_shared_refs()
        self.demonstrate_literal_separate_objects()

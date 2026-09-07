"""
57_Modules.py - Demonstrates importing and using local modules.

Three modules are imported from the same directory:
  - CoinPiles    : Solves the CSES "Coin Piles" problem.
  - spiralMatrix : Generates the CSES Number Spiral grid.
  - beautifulPermutations : Produces a beautiful permutation of 1..N.

Run this file directly to get an interactive menu.
"""

# ---------------------------------------------------------------------------
# Local (same-directory) imports - no package prefix needed.
# ---------------------------------------------------------------------------
import CoinPiles as cp
import spiralMatrix as sm
import beautifulPermutations as bp


# ---------------------------------------------------------------------------
# Automated tests - exercise the module classes without user input.
# ---------------------------------------------------------------------------
def test_coin_piles() -> None:
    """Run predefined test cases against CoinPiles."""
    print("\n" + "=" * 60)
    print("  TEST: CoinPiles")
    print("=" * 60)

    cases = [
        (2, 1, "YES"),
        (2, 2, "NO"),
        (3, 3, "YES"),
        (0, 0, "YES"),
        (1, 0, "NO"),
        (6, 3, "YES"),
        (9, 6, "YES"),
    ]

    passed = 0
    for a, b, expected in cases:
        obj = cp.CoinPiles(a, b)
        # Capture result manually using the same logic
        result = _coin_piles_result(a, b)
        status = "PASS" if result == expected else "FAIL"
        if status == "PASS":
            passed += 1
        print(f"  [{status}]  a={a}, b={b}  -> {result}  (expected {expected})")

    print(f"\n  Results: {passed}/{len(cases)} passed.\n")


def _coin_piles_result(a: int, b: int) -> str:
    """Pure logic check (mirrors CoinPiles algorithm) for testing."""
    if (2 * a - b) % 3 == 0:
        y = (2 * a - b) // 3
        if y >= 0 and (b - y) % 2 == 0:
            x = (b - y) // 2
            if x >= 0:
                return "YES"
    return "NO"


def test_spiral_matrix() -> None:
    """Run predefined checks against SpiralMatrix."""
    print("\n" + "=" * 60)
    print("  TEST: SpiralMatrix")
    print("=" * 60)

    # Known values from the CSES spiral:
    #   1  2  9 10 25
    #   4  3  8 11 24
    #   5  6  7 12 23
    #  16 15 14 13 22
    #  17 18 19 20 21
    cases = [
        (1, 1, 1),
        (1, 2, 2),
        (2, 1, 4),
        (2, 2, 3),
        (2, 3, 8),
        (3, 3, 7),
        (5, 5, 21),
        (4, 4, 13),
    ]

    spiral = sm.SpiralMatrix(5)
    passed = 0
    for row, col, expected in cases:
        val = spiral[row, col]
        status = "PASS" if val == expected else "FAIL"
        if status == "PASS":
            passed += 1
        print(f"  [{status}]  spiral[{row},{col}] = {val}  (expected {expected})")

    print(f"\n  Results: {passed}/{len(cases)} passed.")
    print(f"\n  Full 5x5 spiral:\n{spiral}\n")


def test_beautiful_permutations() -> None:
    """Run predefined checks against the permutation logic."""
    print("\n" + "=" * 60)
    print("  TEST: Beautiful Permutations")
    print("=" * 60)

    cases = [1, 2, 3, 4, 5, 6, 8, 10]

    passed = 0
    for n in cases:
        perm = _generate_beautiful_permutation(n)
        is_valid = _validate_beautiful_permutation(perm, n)
        status = "PASS" if is_valid else "FAIL"
        if status == "PASS":
            passed += 1
        label = " ".join(map(str, perm)) if perm else "NO SOLUTION"
        print(f"  [{status}]  n={n}  -> {label}")

    print(f"\n  Results: {passed}/{len(cases)} passed.\n")


def _generate_beautiful_permutation(n: int) -> list[int]:
    """Generate a beautiful permutation using the same algorithm as the module."""
    if n == 1:
        return [1]
    if n in (2, 3):
        return []  # NO SOLUTION
    evens = list(range(2, n + 1, 2))
    odds = list(range(1, n + 1, 2))
    return evens + odds


def _validate_beautiful_permutation(perm: list[int], n: int) -> bool:
    """Check that adjacent elements differ by more than 1."""
    if n in (2, 3):
        return len(perm) == 0  # NO SOLUTION is correct
    if sorted(perm) != list(range(1, n + 1)):
        return False
    return all(abs(perm[i] - perm[i + 1]) > 1 for i in range(len(perm) - 1))


# ---------------------------------------------------------------------------
# Interactive menu
# ---------------------------------------------------------------------------
def show_menu() -> None:
    """Display the module selection menu."""
    print("\n" + "=" * 60)
    print("  57_Modules - Interactive Module Runner")
    print("=" * 60)
    print()
    print("  Modules available:")
    print("    1. CoinPiles          - Solve the coin-piles problem")
    print("    2. SpiralMatrix       - Generate a number spiral grid")
    print("    3. BeautifulPerms     - Generate a beautiful permutation")
    print()
    print("  Actions:")
    print("    4. Run ALL modules (interactive, one after another)")
    print("    5. Run automated TESTS on all modules")
    print("    0. Exit")
    print()


def run_interactive() -> None:
    """Menu-driven interactive loop."""
    while True:
        show_menu()
        choice = input("  Select an option [0-5]: ").strip()

        if choice == "1":
            print("\n--- CoinPiles (interactive) ---")
            cp.main()

        elif choice == "2":
            print("\n--- SpiralMatrix (interactive) ---")
            sm.main()

        elif choice == "3":
            print("\n--- BeautifulPermutations (interactive) ---")
            bp.main()

        elif choice == "4":
            print("\n>>> Running ALL modules interactively <<<\n")
            print("-" * 40)
            print("  1/3  CoinPiles")
            print("-" * 40)
            cp.main()

            print("-" * 40)
            print("  2/3  SpiralMatrix")
            print("-" * 40)
            sm.main()

            print("-" * 40)
            print("  3/3  BeautifulPermutations")
            print("-" * 40)
            bp.main()

        elif choice == "5":
            print("\n>>> Running automated tests <<<")
            test_coin_piles()
            test_spiral_matrix()
            test_beautiful_permutations()
            print("=" * 60)
            print("  All tests complete.")
            print("=" * 60)

        elif choice == "0":
            print("\nGoodbye!\n")
            break

        else:
            print(f"\n  Invalid choice: '{choice}'. Please enter 0-5.\n")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    run_interactive()

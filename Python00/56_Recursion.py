"""
56_Recursion.py - Demonstrates recursion using the Tower of Hanoi module.

Imports TowerOfHanoi and provides an interactive entry point.
"""

import TowerOfHanoi as TH


def main() -> None:
    """Interactive entry point: prompt for disk count and solve."""
    n: int = int(input("Enter the number of disks: "))
    tower = TH.TowerOfHanoi(n)
    tower.solve()


if __name__ == "__main__":
    main()

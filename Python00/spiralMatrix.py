"""
CSES Number Spiral — OOP implementation.

The number spiral fills an infinite grid where:
  - Odd-indexed layers spiral downward then right.
  - Even-indexed layers spiral right then downward.

Each cell value is computed in O(1) using a closed-form formula,
so the matrix is never stored — it's generated on the fly.
"""

from __future__ import annotations

from typing import Iterator


class SpiralMatrix:
    """Represents an N×N CSES Number Spiral.

    The matrix is *virtual*: no N×N array is allocated.
    Each value is computed in O(1) via a closed-form formula,
    making this memory-efficient even for very large N.

    Usage:
        >>> spiral = SpiralMatrix(5)
        >>> spiral[1, 1]      # top-left cell
        1
        >>> spiral[2, 3]      # row 2, column 3
        8
        >>> print(spiral)     # pretty-printed grid
    """

    __slots__ = ("_size",)

    def __init__(self, size: int) -> None:
        if not isinstance(size, int) or size <= 0:
            raise ValueError(f"Size must be a positive integer, got {size!r}")
        self._size = size

    # ---- Properties ----------------------------------------------------------

    @property
    def size(self) -> int:
        """Grid dimension (N×N)."""
        return self._size

    @property
    def max_value(self) -> int:
        """Largest value in the grid (N²)."""
        return self._size * self._size

    # ---- Core formula --------------------------------------------------------

    @staticmethod
    def value_at(row: int, col: int) -> int:
        """Return the spiral value at 1-based (row, col) in O(1).

        The formula exploits the layer structure of the spiral:
        layer = max(row, col) determines which concentric "ring"
        the cell belongs to. Within each layer the values are
        laid out linearly, alternating direction for odd/even layers.

        Args:
            row: 1-based row index.
            col: 1-based column index.

        Returns:
            The integer value at (row, col).
        """
        layer = max(row, col)
        layer_start = (layer - 1) ** 2  # last value of previous layer

        if layer & 1:  # odd layer — column edge
            return layer * layer - (row - 1) if col == layer else layer_start + col
        else:          # even layer — row edge
            return layer * layer - (col - 1) if row == layer else layer_start + row

    # ---- Dunder methods ------------------------------------------------------

    def __getitem__(self, index: tuple[int, int]) -> int:
        """Enable ``spiral[row, col]`` access with bounds checking."""
        row, col = index
        if not (1 <= row <= self._size and 1 <= col <= self._size):
            raise IndexError(
                f"({row}, {col}) is out of bounds for a {self._size}×{self._size} spiral"
            )
        return self.value_at(row, col)

    def __iter__(self) -> Iterator[list[int]]:
        """Yield one row at a time as a list of ints."""
        for r in range(1, self._size + 1):
            yield [self.value_at(r, c) for c in range(1, self._size + 1)]

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(size={self._size})"

    def __str__(self) -> str:
        """Pretty-print the spiral with right-aligned columns."""
        width = len(str(self.max_value)) + 1
        lines: list[str] = []
        for row in self:
            lines.append("".join(str(v).rjust(width) for v in row))
        return "\n".join(lines)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, SpiralMatrix):
            return NotImplemented
        return self._size == other._size

    def __hash__(self) -> int:
        return hash(self._size)


# ---- Entry point -------------------------------------------------------------

def main() -> None:
    """Interactive entry point: prompt for N, display the spiral."""
    try:
        n = int(input("Enter grid size N (prints 1 to N rows/cols): "))
        spiral = SpiralMatrix(n)
        print(f"\nCSES Number Spiral ({spiral.size}x{spiral.size}):\n")
        print(spiral)
    except ValueError as err:
        print(f"Invalid input: {err}")


if __name__ == "__main__":
    main()
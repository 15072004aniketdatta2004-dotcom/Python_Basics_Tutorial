import sys


def solve() -> None:
  # readline() reads a single line immediately on pressing Enter
  line = sys.stdin.readline().strip()
  if not line:
    return

  n = int(line)

  # Base Case: n = 1 is trivially beautiful
  if n == 1:
    sys.stdout.write("1\n")
    return

  # Impossible Cases: n = 2 and n = 3 have no valid permutation
  if n in [2, 3]:
    sys.stdout.write("NO SOLUTION\n")
    return

  # Construction: Evens followed by Odds
  # Evens: 2 4 6 ...
  # Odds:  1 3 5 ...
  # Internal diff is always 2. Seam diff: |evens[-1] - 1| >= 3 > 1 for n >= 4.
  write = sys.stdout.write
  buffer = []
  CHUNK_SIZE = 50000

  for x in range(2, n + 1, 2):
    buffer.append(str(x))
    if len(buffer) >= CHUNK_SIZE:
      write(" ".join(buffer) + " ")
      buffer.clear()

  for x in range(1, n + 1, 2):
    buffer.append(str(x))
    if len(buffer) >= CHUNK_SIZE:
      write(" ".join(buffer) + " ")
      buffer.clear()

  if buffer:
    write(" ".join(buffer))

  write("\n")


def main() -> None:
    """Interactive entry point for beautiful permutations."""
    print("=== Beautiful Permutations ===")
    print("Enter N to get a beautiful permutation (adjacent elements differ by more than 1).")
    solve()


if __name__ == "__main__":
    main()
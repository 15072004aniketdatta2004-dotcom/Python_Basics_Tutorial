import sys
from io import StringIO

# ============================================================
# String Buffer in Python
# ============================================================
# Python has NO built-in StringBuffer like Java/C#.
# Instead, we use `io.StringIO` — an in-memory text stream.
#
# MEMORY LAYOUT of StringIO:
# ┌──────────────────────────────────────────────┐
# │  StringIO Object                             │
# │  ┌─────┬─────┬───────┬──────────────────┐    │
# │  │"Hel"│"lo "│"World"│ (dynamic growth) │    │
# │  └─────┴─────┴───────┴──────────────────┘    │
# │  position cursor ──▶ points after last write │
# │  getvalue() → joins chunks → "Hello World"   │
# └──────────────────────────────────────────────┘
#
# KEY DIFFERENCE FROM JAVA:
# - Java StringBuffer: pre-allocates char[] with capacity (default 16)
# - Python StringIO:   dynamically grows, NO explicit capacity API
# - To enforce capacity in Python, we must do it manually (see below)
# ============================================================


class StringBuffer:
    """
    A string buffer with optional capacity limit.

    Capacity Behavior:
        - capacity=None → unlimited (like default StringIO)
        - capacity=N    → max N characters allowed in the buffer

    Memory: Internally uses StringIO which stores text in a
    contiguous memory block (similar to a list of characters).
    """

    def __init__(self, capacity: int = None, initial: str = ""):
        """
        Create a StringBuffer.

        Args:
            capacity: Max number of characters (None = unlimited).
                      Similar to Java's `new StringBuffer(capacity)`.
            initial:  Initial string to put in the buffer.
                      Similar to Java's `new StringBuffer("text")`.
        """
        self.buffer = StringIO()
        self._capacity = capacity  # None means unlimited

        if initial:
            self.append(initial)

    # --- Capacity Management ---

    @property
    def capacity(self) -> int | None:
        """Get the current capacity (None = unlimited)."""
        return self._capacity

    @capacity.setter
    def capacity(self, new_capacity: int | None):
        """
        Set new capacity. If current content exceeds it, truncates.

        Example:
            buf = StringBuffer(capacity=100)
            buf.capacity = 50   # shrinks capacity, truncates if needed
            buf.capacity = None  # removes limit entirely
        """
        if new_capacity is not None and new_capacity < 0:
            raise ValueError("Capacity must be non-negative or None")
        self._capacity = new_capacity
        # Truncate if content exceeds new capacity
        if self._capacity is not None:
            current = self.buffer.getvalue()
            if len(current) > self._capacity:
                self.buffer = StringIO()
                self.buffer.write(current[:self._capacity])

    # --- Core Operations ---

    def append(self, s: str) -> "StringBuffer":
        """
        Append a string. Respects capacity if set.
        Returns self for chaining: buf.append("a").append("b")
        """
        if self._capacity is not None:
            current_len = len(self.buffer.getvalue())
            remaining = self._capacity - current_len
            if remaining <= 0:
                return self  # buffer is full
            s = s[:remaining]  # trim to fit capacity
        self.buffer.write(s)
        return self

    def insert(self, index: int, s: str) -> "StringBuffer":
        """Insert string at a specific position."""
        current = self.buffer.getvalue()
        new_content = current[:index] + s + current[index:]
        if self._capacity is not None:
            new_content = new_content[:self._capacity]
        self.buffer = StringIO()
        self.buffer.write(new_content)
        return self

    def delete(self, start: int, end: int) -> "StringBuffer":
        """Delete characters from start to end (exclusive)."""
        current = self.buffer.getvalue()
        new_content = current[:start] + current[end:]
        self.buffer = StringIO()
        self.buffer.write(new_content)
        return self

    def reverse(self) -> "StringBuffer":
        """Reverse the buffer contents."""
        current = self.buffer.getvalue()
        self.buffer = StringIO()
        self.buffer.write(current[::-1])
        return self

    def clear(self):
        """Clear the buffer (reset to empty)."""
        self.buffer.seek(0)
        self.buffer.truncate()

    # --- Info Methods ---

    def length(self) -> int:
        """Current number of characters in the buffer."""
        return len(self.buffer.getvalue())

    def remaining(self) -> int | None:
        """How many more chars can fit (None if unlimited)."""
        if self._capacity is None:
            return None
        return self._capacity - self.length()

    def is_full(self) -> bool:
        """Check if buffer has reached capacity."""
        if self._capacity is None:
            return False
        return self.length() >= self._capacity

    def memory_info(self) -> dict:
        """
        Show how this buffer looks in memory.

        Returns dict with:
            - content: the actual string
            - length: number of characters
            - capacity: max chars allowed (None = unlimited)
            - remaining: space left
            - size_bytes: actual memory used by the string
            - object_size: memory used by StringIO object
        """
        content = self.buffer.getvalue()
        return {
            "content": repr(content),
            "length": len(content),
            "capacity": self._capacity,
            "remaining": self.remaining(),
            "size_bytes_string": sys.getsizeof(content),
            "size_bytes_stringio": sys.getsizeof(self.buffer),
        }

    def visualize_memory(self):
        """Print a visual representation of the buffer in memory."""
        content = self.buffer.getvalue()
        length = len(content)
        cap = self._capacity
        str_bytes = sys.getsizeof(content)
        io_bytes = sys.getsizeof(self.buffer)

        print("=" * 55)
        print("  STRING BUFFER — MEMORY VISUALIZATION")
        print("=" * 55)

        # Show the buffer contents
        if cap is not None:
            used_bar = "█" * min(length, 40)
            free_bar = "░" * min(cap - length, 40 - min(length, 40))
            print(f"  Buffer:  [{used_bar}{free_bar}]")
            print(f"  Used:    {length}/{cap} chars "
                  f"({length/cap*100:.0f}% full)")
        else:
            used_bar = "█" * min(length, 40)
            print(f"  Buffer:  [{used_bar}→∞]")
            print(f"  Used:    {length} chars (unlimited capacity)")

        # Show content preview
        preview = content[:50]
        if len(content) > 50:
            preview += "..."
        print(f'  Content: "{preview}"')

        # Memory usage
        print(f"  Memory:  {str_bytes} bytes (string) "
              f"+ {io_bytes} bytes (StringIO)")
        print("=" * 55)

    def __str__(self):
        return self.buffer.getvalue()

    def __len__(self):
        return self.length()

    def __repr__(self):
        return (f"StringBuffer(length={self.length()}, "
                f"capacity={self._capacity})")


# ============================================================
# DEMO: How to use capacity & see memory layout
# ============================================================
if __name__ == "__main__":

    # --- 1. Unlimited capacity (default, like StringIO) ---
    print("\n>> 1. Unlimited Buffer (no capacity limit)")
    buf = StringBuffer()
    buf.append("Hello ").append("World!")
    print(f"   Content: {buf}")
    print(f"   Info: {buf.memory_info()}")
    buf.visualize_memory()

    # --- 2. Set capacity at creation ---
    print("\n>> 2. Buffer with capacity=20")
    buf2 = StringBuffer(capacity=20, initial="Python")
    buf2.append(" is awesome and great!")  # will be trimmed!
    print(f"   Content: {buf2}")
    print(f"   Is full? {buf2.is_full()}")
    print(f"   Remaining: {buf2.remaining()} chars")
    buf2.visualize_memory()

    # --- 3. Change capacity dynamically ---
    print("\n>> 3. Change capacity at runtime")
    buf3 = StringBuffer(initial="Hello World")
    print(f"   Before: '{buf3}' (capacity={buf3.capacity})")

    buf3.capacity = 5  # shrinks! truncates content
    print(f"   After setting capacity=5: '{buf3}'")
    buf3.visualize_memory()

    buf3.capacity = None  # remove limit
    buf3.append(" — Now unlimited!")
    print(f"   After removing limit: '{buf3}'")
    buf3.visualize_memory()

    # --- 4. Memory comparison: String concat vs StringBuffer ---
    print("\n>> 4. Memory: String concat vs StringBuffer")
    # BAD: String concatenation (creates new object each time)
    s = ""
    for i in range(100):
        s += "x"  # each += creates a NEW string in memory!
    print(f"   String concat: {sys.getsizeof(s)} bytes for {len(s)} chars")

    # GOOD: StringBuffer (reuses internal buffer)
    buf4 = StringBuffer()
    for i in range(100):
        buf4.append("x")  # writes to SAME buffer in memory
    print(f"   StringBuffer:  {buf4.memory_info()['size_bytes_string']} bytes "
          f"for {buf4.length()} chars")
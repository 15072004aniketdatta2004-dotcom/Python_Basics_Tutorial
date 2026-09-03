"""
================================================================================
  PYTHON LOOPS INTERNALS — BEHIND THE SCENES
  Topics: Iteration Protocol, Iterables, Iterators, __next__(), __iter__(),
          Generators, itertools, and how for-loops REALLY work.
================================================================================
"""

# ══════════════════════════════════════════════════════════════════════════════
# 1. THE ITERATION PROTOCOL — The Foundation
# ══════════════════════════════════════════════════════════════════════════════
#
# In Python, loops are NOT driven by index counting (like C's for(i=0; i<n; i++)).
# Instead, Python uses the **Iteration Protocol**, which consists of two methods:
#
#   __iter__()  → Returns an iterator object (often self)
#   __next__()  → Returns the next value, raises StopIteration when exhausted
#
# Every for-loop in Python secretly uses this protocol.

print("=" * 60)
print("  1. THE ITERATION PROTOCOL")
print("=" * 60)

# ── 1a. Iterable vs Iterator ──
# 
# ITERABLE: Any object that has an __iter__() method.
#           Examples: list, tuple, str, dict, set, range, file objects
#           An iterable can be looped over MULTIPLE times.
#
# ITERATOR: Any object that has BOTH __iter__() and __next__() methods.
#           It remembers its position (state). It can only be consumed ONCE.
#           __iter__() on an iterator returns itself.

my_list = [10, 20, 30]

# Check: is it iterable?
print(f"\nmy_list = {my_list}")
print(f"  Has __iter__? {hasattr(my_list, '__iter__')}")   # True — it's ITERABLE
print(f"  Has __next__? {hasattr(my_list, '__next__')}")   # False — it's NOT an ITERATOR

# Get an iterator FROM the iterable
my_iterator = iter(my_list)   # Calls my_list.__iter__() internally
print(f"\nmy_iterator = iter(my_list)")
print(f"  type(my_iterator) = {type(my_iterator)}")
print(f"  Has __iter__? {hasattr(my_iterator, '__iter__')}")  # True
print(f"  Has __next__? {hasattr(my_iterator, '__next__')}")  # True — NOW it's an ITERATOR

# iter() on an iterator returns ITSELF (identity)
print(f"  iter(my_iterator) is my_iterator? {iter(my_iterator) is my_iterator}")  # True


# ── 1b. Manual Iteration with __next__() ──
print("\n── Manual Iteration with next() ──")

it = iter([10, 20, 30])
print(f"  next(it) = {next(it)}")    # 10  — calls it.__next__()
print(f"  next(it) = {next(it)}")    # 20
print(f"  next(it) = {next(it)}")    # 30
# next(it) here would raise StopIteration!
# Using a default value to avoid the exception:
print(f"  next(it, 'EXHAUSTED') = {next(it, 'EXHAUSTED')}")  # 'EXHAUSTED'


# ── 1c. What a for-loop ACTUALLY does ──
print("\n── What 'for x in [10, 20, 30]:' ACTUALLY does ──")

# This:
#   for x in [10, 20, 30]:
#       print(x)
#
# Is EXACTLY equivalent to:

_iterable = [10, 20, 30]
_iterator = iter(_iterable)       # Step 1: Get iterator via __iter__()
while True:
    try:
        x = next(_iterator)       # Step 2: Call __next__() each iteration
    except StopIteration:         # Step 3: Catch StopIteration to end loop
        break
    print(f"  x = {x}")           # Step 4: Execute loop body

# Python's for-loop is just syntactic sugar for this pattern!


# ══════════════════════════════════════════════════════════════════════════════
# 2. ITERABLE OBJECTS — What Can You Iterate Over?
# ══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("  2. ITERABLE OBJECTS IN PYTHON")
print("=" * 60)

# ── 2a. Strings are iterable (character by character) ──
print("\n── String Iteration ──")
s = "HELLO"
s_iter = iter(s)
print(f"  iter('HELLO'): {next(s_iter)}, {next(s_iter)}, {next(s_iter)}, {next(s_iter)}, {next(s_iter)}")

# ── 2b. Dictionaries are iterable (over keys by default) ──
print("\n── Dictionary Iteration ──")
d = {"a": 1, "b": 2, "c": 3}
print(f"  dict keys:   ", end="")
for key in d:                     # Iterates over KEYS
    print(key, end=" ")
print()

print(f"  dict values: ", end="")
for val in d.values():            # .values() returns an iterable of values
    print(val, end=" ")
print()

print(f"  dict items:  ", end="")
for k, v in d.items():            # .items() returns (key, value) tuples
    print(f"{k}:{v}", end=" ")
print()

# ── 2c. range() is iterable but NOT a list ──
print("\n── range() Object ──")
r = range(5)
print(f"  type(range(5)) = {type(r)}")
print(f"  Has __iter__? {hasattr(r, '__iter__')}")
print(f"  Has __next__? {hasattr(r, '__next__')}")   # False! range is iterable, NOT an iterator
print(f"  Memory: range(1000000) doesn't store 1M numbers — it computes them on the fly")

# ── 2d. File objects are iterators (they iterate line by line) ──
print("\n── File Object Iteration ──")
# Writing a temp file to demonstrate
with open("_temp_demo.txt", "w") as f:
    f.write("Line 1\nLine 2\nLine 3\n")

with open("_temp_demo.txt", "r") as f:
    print(f"  type(f)        = {type(f)}")
    print(f"  Has __iter__?  {hasattr(f, '__iter__')}")  # True
    print(f"  Has __next__?  {hasattr(f, '__next__')}")  # True — file IS an iterator!
    print(f"  f.readline()   = {f.readline().strip()}")   # Line 1
    print(f"  next(f)        = {next(f).strip()}")        # Line 2
    print(f"  next(f)        = {next(f).strip()}")        # Line 3
    # readline() and next() both advance the SAME internal position pointer

import os
os.remove("_temp_demo.txt")  # cleanup

# ── 2e. Iterators are single-use! ──
print("\n── Iterators Are Single-Use ──")
nums = [1, 2, 3]
it = iter(nums)
first_pass  = list(it)   # Consumes the iterator
second_pass = list(it)   # Empty! Already exhausted
print(f"  first_pass  = {first_pass}")    # [1, 2, 3]
print(f"  second_pass = {second_pass}")   # []
print("  ⚠ Once an iterator is exhausted, it stays empty — you need a NEW iterator!")


# ══════════════════════════════════════════════════════════════════════════════
# 3. BUILDING CUSTOM ITERATORS — The __iter__ / __next__ Protocol
# ══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("  3. CUSTOM ITERATORS")
print("=" * 60)

# ── 3a. A simple counter iterator ──
print("\n── Custom CountUp Iterator ──")

class CountUp:
    """Iterator that counts from 'start' up to 'end' (inclusive)."""
    def __init__(self, start: int, end: int):
        self.current = start
        self.end = end
    
    def __iter__(self):
        """Return self — this object IS the iterator."""
        return self
    
    def __next__(self):
        """Return next value or raise StopIteration."""
        if self.current > self.end:
            raise StopIteration          # Signal: no more values
        value = self.current
        self.current += 1
        return value

# Using our custom iterator in a for-loop:
print("  CountUp(1, 5): ", end="")
for num in CountUp(1, 5):
    print(num, end=" ")
print()

# Manual iteration:
counter = CountUp(10, 12)
print(f"  next(CountUp(10,12)) = {next(counter)}")  # 10
print(f"  next(CountUp(10,12)) = {next(counter)}")  # 11
print(f"  next(CountUp(10,12)) = {next(counter)}")  # 12


# ── 3b. Fibonacci Iterator (infinite) ──
print("\n── Fibonacci Iterator (first 10 values) ──")

class Fibonacci:
    """Infinite iterator that yields Fibonacci numbers."""
    def __init__(self):
        self.a, self.b = 0, 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        value = self.a
        self.a, self.b = self.b, self.a + self.b  # Simultaneous assignment
        return value

fib = Fibonacci()
fib_10 = [next(fib) for _ in range(10)]
print(f"  First 10 Fibonacci: {fib_10}")


# ── 3c. Making an Iterable (not iterator) class ──
print("\n── Iterable vs Iterator Class ──")

class ReusableRange:
    """An ITERABLE (not iterator) — can be looped over multiple times.
    Each call to __iter__() returns a FRESH iterator."""
    def __init__(self, n: int):
        self.n = n
    
    def __iter__(self):
        """Return a new iterator each time — this makes it reusable."""
        return self._Iterator(self.n)
    
    class _Iterator:
        """The actual iterator — single-use."""
        def __init__(self, n):
            self.current = 0
            self.n = n
        def __iter__(self):
            return self
        def __next__(self):
            if self.current >= self.n:
                raise StopIteration
            val = self.current
            self.current += 1
            return val

rr = ReusableRange(4)
print(f"  First loop:  {list(rr)}")    # [0, 1, 2, 3]
print(f"  Second loop: {list(rr)}")    # [0, 1, 2, 3] — works again!
print("  ✓ Because __iter__() returns a NEW _Iterator each time.")


# ══════════════════════════════════════════════════════════════════════════════
# 4. GENERATORS — Simplified Iterators
# ══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("  4. GENERATORS — Lazy Iterators Made Easy")
print("=" * 60)

# A generator is a function that uses 'yield' instead of 'return'.
# When called, it returns a generator object (which IS an iterator).
# It PAUSES execution at each yield and RESUMES when next() is called.

# ── 4a. Generator function ──
print("\n── Generator Function ──")

def count_up_gen(start, end):
    """Generator version of CountUp — much simpler!"""
    current = start
    while current <= end:
        yield current       # Pauses here, returns value
        current += 1        # Resumes here on next(call)
    # When function ends, StopIteration is raised automatically

gen = count_up_gen(1, 5)
print(f"  type(gen) = {type(gen)}")
print(f"  Is iterator? Has __next__: {hasattr(gen, '__next__')}")
print(f"  count_up_gen(1,5): ", end="")
for n in count_up_gen(1, 5):
    print(n, end=" ")
print()


# ── 4b. Generator Expressions (like list comprehensions, but lazy) ──
print("\n── Generator Expressions ──")

# List comprehension — builds the ENTIRE list in memory
squares_list = [x**2 for x in range(5)]
print(f"  List comp: {squares_list}, type={type(squares_list).__name__}")

# Generator expression — computes values ONE AT A TIME
squares_gen = (x**2 for x in range(5))
print(f"  Gen expr:  {squares_gen}, type={type(squares_gen).__name__}")
print(f"  next():    {next(squares_gen)}, {next(squares_gen)}, {next(squares_gen)}")
print(f"  remaining: {list(squares_gen)}")   # Only unconsumed values

# Memory comparison
import sys
big_list = [x for x in range(10000)]
big_gen  = (x for x in range(10000))
print(f"\n  Memory of list(10000): {sys.getsizeof(big_list)} bytes")
print(f"  Memory of gen(10000):  {sys.getsizeof(big_gen)} bytes")
print("  ✓ Generators use constant memory regardless of size!")


# ── 4c. yield from — Delegating to sub-iterators ──
print("\n── yield from (Sub-generator Delegation) ──")

def flatten(nested_list):
    """Recursively flatten a nested list using yield from."""
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten(item)  # Delegate to recursive call
        else:
            yield item

nested = [1, [2, 3], [4, [5, 6]], 7]
print(f"  Nested:    {nested}")
print(f"  Flattened: {list(flatten(nested))}")


# ── 4d. Generator .send(), .throw(), .close() ──
print("\n── Generator .send() — Two-way Communication ──")

def accumulator():
    """Generator that accumulates values sent to it."""
    total = 0
    while True:
        value = yield total    # yield current total, receive next value
        if value is None:
            break
        total += value

acc = accumulator()
next(acc)                        # Prime the generator (advance to first yield)
print(f"  send(10) → {acc.send(10)}")   # total = 10
print(f"  send(20) → {acc.send(20)}")   # total = 30
print(f"  send(5)  → {acc.send(5)}")    # total = 35
acc.close()                      # Gracefully stop the generator


# ══════════════════════════════════════════════════════════════════════════════
# 5. ITERTOOLS — The Iteration Power Tools
# ══════════════════════════════════════════════════════════════════════════════

import itertools

print("\n" + "=" * 60)
print("  5. ITERTOOLS MODULE")
print("=" * 60)

# ── 5a. Infinite Iterators ──
print("\n── 5a. Infinite Iterators ──")

# count(start, step) — counts forever
counter = itertools.count(10, 3)
print(f"  count(10, 3): {next(counter)}, {next(counter)}, {next(counter)}, {next(counter)}")
# → 10, 13, 16, 19

# cycle(iterable) — repeats forever
cycler = itertools.cycle(['A', 'B', 'C'])
cycle_vals = [next(cycler) for _ in range(7)]
print(f"  cycle('ABC') × 7: {cycle_vals}")
# → ['A', 'B', 'C', 'A', 'B', 'C', 'A']

# repeat(val, n) — repeat a value n times (or forever if n omitted)
print(f"  repeat('X', 4): {list(itertools.repeat('X', 4))}")


# ── 5b. Terminating Iterators ──
print("\n── 5b. Terminating Iterators ──")

# chain(*iterables) — concatenate multiple iterables
print(f"  chain([1,2], [3,4], [5]): {list(itertools.chain([1,2], [3,4], [5]))}")

# chain.from_iterable — chain from a single iterable of iterables
print(f"  chain.from_iterable: {list(itertools.chain.from_iterable([[1,2],[3,4],[5,6]]))}")

# islice(iterable, stop) or islice(iterable, start, stop, step) — slice any iterator
fib2 = Fibonacci()
print(f"  islice(Fibonacci, 8): {list(itertools.islice(fib2, 8))}")

# takewhile(predicate, iterable) — take while condition is True
print(f"  takewhile(x<5, range(10)): {list(itertools.takewhile(lambda x: x < 5, range(10)))}")

# dropwhile(predicate, iterable) — skip while condition is True, then take the rest
print(f"  dropwhile(x<5, range(10)): {list(itertools.dropwhile(lambda x: x < 5, range(10)))}")

# filterfalse(predicate, iterable) — opposite of filter()
print(f"  filterfalse(is_even, 0..7): {list(itertools.filterfalse(lambda x: x % 2, range(8)))}")

# compress(data, selectors) — filter by boolean mask
data = ['A', 'B', 'C', 'D', 'E']
mask = [1, 0, 1, 0, 1]
print(f"  compress({data}, {mask}): {list(itertools.compress(data, mask))}")

# accumulate(iterable, func) — running totals (or other running operations)
print(f"  accumulate([1,2,3,4,5]):     {list(itertools.accumulate([1,2,3,4,5]))}")
print(f"  accumulate([1,2,3,4], mul):  {list(itertools.accumulate([1,2,3,4], lambda a,b: a*b))}")

# zip_longest — like zip but pads shorter iterables
print(f"  zip_longest([1,2,3],[a,b]): {list(itertools.zip_longest([1,2,3],['a','b'], fillvalue='?'))}")

# starmap(func, iterable_of_tuples) — unpacks args from tuples
print(f"  starmap(pow, [(2,3),(3,2)]): {list(itertools.starmap(pow, [(2,3),(3,2),(10,3)]))}")

# tee(iterable, n) — clone an iterator into n independent copies
original = iter(range(4))
copy1, copy2 = itertools.tee(original, 2)
print(f"  tee(range(4), 2): copy1={list(copy1)}, copy2={list(copy2)}")

# pairwise (Python 3.10+) — consecutive pairs
print(f"  pairwise([1,2,3,4,5]): {list(itertools.pairwise([1,2,3,4,5]))}")

# batched (Python 3.12+) — split into fixed-size chunks
print(f"  batched('ABCDEFG', 3): {list(itertools.batched('ABCDEFG', 3))}")


# ── 5c. Combinatoric Iterators ──
print("\n── 5c. Combinatoric Iterators ──")

# product — Cartesian product (like nested for-loops)
print(f"  product([1,2], ['a','b']): {list(itertools.product([1,2], ['a','b']))}")
print(f"  product('AB', repeat=2):  {list(itertools.product('AB', repeat=2))}")

# permutations — ordered arrangements
print(f"  permutations('ABC', 2):   {list(itertools.permutations('ABC', 2))}")

# combinations — unordered selections (no repeats)
print(f"  combinations('ABCD', 2):  {list(itertools.combinations('ABCD', 2))}")

# combinations_with_replacement — unordered selections (with repeats)
print(f"  combinations_w_rep('AB',3): {list(itertools.combinations_with_replacement('AB', 3))}")


# ── 5d. groupby — Group consecutive elements ──
print("\n── 5d. groupby ──")

data = [("fruit", "apple"), ("fruit", "banana"), ("veg", "carrot"), ("veg", "pea"), ("fruit", "mango")]
# IMPORTANT: data must be sorted by the key for groupby to work correctly!
data.sort(key=lambda x: x[0])
for key, group in itertools.groupby(data, key=lambda x: x[0]):
    items = [item[1] for item in group]
    print(f"  {key}: {items}")


# ══════════════════════════════════════════════════════════════════════════════
# 6. BUILT-IN ITERATION FUNCTIONS
# ══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("  6. BUILT-IN ITERATION FUNCTIONS")
print("=" * 60)

# ── map(func, iterable) — apply function to each element ──
print(f"\n  map(str.upper, ['hi','bye']): {list(map(str.upper, ['hi', 'bye']))}")

# ── filter(func, iterable) — keep elements where func returns True ──
print(f"  filter(is_even, 0..9): {list(filter(lambda x: x % 2 == 0, range(10)))}")

# ── zip(iter1, iter2, ...) — pair up elements ──
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
print(f"  zip(names, scores): {list(zip(names, scores))}")

# ── enumerate(iterable, start=0) — add index ──
print("  enumerate(['a','b','c']):")
for i, val in enumerate(['a', 'b', 'c'], start=1):
    print(f"    {i}: {val}")

# ── reversed(seq) — reverse iteration (needs __reversed__ or __len__+__getitem__) ──
print(f"  reversed([1,2,3,4,5]): {list(reversed([1,2,3,4,5]))}")

# ── sorted(iterable) — returns sorted list from any iterable ──
print(f"  sorted({{3,1,4,1,5}}): {sorted({3,1,4,1,5})}")

# ── any() and all() — short-circuit boolean checks ──
print(f"  any([0, '', None, 42]): {any([0, '', None, 42])}")   # True (42 is truthy)
print(f"  all([1, 'hi', True]):   {all([1, 'hi', True])}")     # True
print(f"  all([1, 'hi', 0]):      {all([1, 'hi', 0])}")        # False (0 is falsy)

# ── sum(), min(), max() — all work with iterables ──
gen = (x**2 for x in range(5))
print(f"  sum(x² for x in range(5)): {sum(x**2 for x in range(5))}")
print(f"  min & max of [3,1,4,1,5]:  min={min([3,1,4,1,5])}, max={max([3,1,4,1,5])}")


# ══════════════════════════════════════════════════════════════════════════════
# 7. ADVANCED INTERNALS — Under the Hood
# ══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("  7. ADVANCED INTERNALS")
print("=" * 60)

# ── 7a. The __getitem__ fallback ──
print("\n── 7a. __getitem__ Fallback Protocol ──")
# If an object has NO __iter__ but HAS __getitem__, Python will still
# iterate over it by calling __getitem__(0), __getitem__(1), ... until IndexError.

class OldStyleIterable:
    """Pre-iterator-protocol object — uses __getitem__ only."""
    def __init__(self, data):
        self.data = data
    def __getitem__(self, index):
        return self.data[index]    # IndexError when out of range stops iteration

old = OldStyleIterable([100, 200, 300])
print(f"  OldStyleIterable (no __iter__): {list(old)}")  # [100, 200, 300] — still works!
print(f"  Has __iter__? {hasattr(old, '__iter__')}")      # False!
print("  ✓ Python falls back to __getitem__(0), (1), (2), ... IndexError → stop")


# ── 7b. Iterator state inspection ──
print("\n── 7b. Iterator State ──")

it = iter([10, 20, 30])
print(f"  After iter():   id={id(it)}")
print(f"  next() → {next(it)}")
print(f"  After 1 next(): id={id(it)} (same object, internal state changed)")
# The iterator object doesn't change identity — only its internal position moves.


# ── 7c. StopIteration propagation ──
print("\n── 7c. StopIteration ──")

def demo_stopiteration():
    it = iter([42])
    print(f"  next(it) = {next(it)}")   # 42
    try:
        val = next(it)                   # Raises StopIteration
    except StopIteration as e:
        print(f"  StopIteration caught! value={e.value}")
        # e.value is None by default, but generators can set it via 'return value'

demo_stopiteration()

# Generator with a return value:
def gen_with_return():
    yield 1
    yield 2
    return "DONE"   # This becomes StopIteration.value

g = gen_with_return()
print(f"\n  Generator with return value:")
print(f"  next(g) = {next(g)}")
print(f"  next(g) = {next(g)}")
try:
    next(g)
except StopIteration as e:
    print(f"  StopIteration.value = '{e.value}'")  # 'DONE'


# ── 7d. Sentinel form of iter() ──
print("\n── 7d. iter(callable, sentinel) — The Two-Argument Form ──")

# iter(callable, sentinel) calls callable() repeatedly until it returns sentinel.
import random
random.seed(42)  # For reproducibility
# Read random digits until we get a 5:
results = list(iter(lambda: random.randint(0, 9), 5))
print(f"  iter(random_digit, sentinel=5): {results}")
print("  ✓ Stops as soon as 5 is generated (5 itself NOT included)")


# ── 7e. How 'in' operator uses iteration ──
print("\n── 7e. 'in' Operator and Iteration ──")
# 'x in iterable' uses __contains__ if available, otherwise falls back to iteration.
# For iterators (no __contains__), it CONSUMES elements until found!

it = iter(range(10))
print(f"  5 in iter(range(10)): {5 in it}")     # True — consumed 0,1,2,3,4,5
print(f"  Remaining after 'in': {list(it)}")     # [6, 7, 8, 9] — first 6 consumed!
print("  ⚠ 'in' on iterators is destructive — it consumes elements!")


# ══════════════════════════════════════════════════════════════════════════════
# 8. PRACTICAL PATTERNS
# ══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("  8. PRACTICAL ITERATION PATTERNS")
print("=" * 60)

# ── 8a. Chunking an iterable ──
print("\n── 8a. Chunking ──")

def chunked(iterable, size):
    """Yield successive chunks of 'size' from iterable."""
    it = iter(iterable)
    while True:
        chunk = list(itertools.islice(it, size))
        if not chunk:
            break
        yield chunk

print(f"  chunked(range(10), 3): {list(chunked(range(10), 3))}")

# ── 8b. Sliding window ──
print("\n── 8b. Sliding Window ──")

def sliding_window(iterable, n):
    """Yield overlapping windows of size n."""
    it = iter(iterable)
    window = list(itertools.islice(it, n))
    if len(window) == n:
        yield tuple(window)
    for item in it:
        window = window[1:] + [item]
        yield tuple(window)

print(f"  sliding_window([1,2,3,4,5], 3): {list(sliding_window([1,2,3,4,5], 3))}")

# ── 8c. Enumerate with unpacking ──
print("\n── 8c. Parallel Iteration ──")
names = ["Alice", "Bob", "Charlie"]
ages  = [30, 25, 35]
cities = ["NYC", "LA", "Chicago"]
print("  zip(names, ages, cities):")
for name, age, city in zip(names, ages, cities):
    print(f"    {name}, age {age}, from {city}")


# ══════════════════════════════════════════════════════════════════════════════
# 9. SUMMARY — The Complete Picture
# ══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("  9. SUMMARY")
print("=" * 60)
print("""
  ┌──────────────────────────────────────────────────────────┐
  │                  ITERATION HIERARCHY                     │
  │                                                          │
  │  Iterable ──→ has __iter__() → returns an Iterator       │
  │     │                                                    │
  │     ├── list, tuple, str, dict, set, range, frozenset    │
  │     ├── file objects (also iterators)                     │
  │     ├── Custom classes with __iter__()                    │
  │     └── Objects with __getitem__() (fallback)            │
  │                                                          │
  │  Iterator ──→ has __iter__() AND __next__()              │
  │     │                                                    │
  │     ├── iter(list), iter(str), etc.                      │
  │     ├── Generator objects (from yield functions)         │
  │     ├── Generator expressions  (x for x in ...)         │
  │     ├── map(), filter(), zip(), enumerate() objects      │
  │     ├── File objects                                     │
  │     └── itertools objects (chain, islice, etc.)          │
  │                                                          │
  │  for x in obj:     →  __iter__()  →  __next__() loop    │
  │  next(iterator)    →  __next__() directly                │
  │  StopIteration     →  signals end of iteration           │
  └──────────────────────────────────────────────────────────┘

  Key Takeaways:
  • Every for-loop uses __iter__ + __next__ + StopIteration
  • Iterables can be looped multiple times; iterators only once
  • Generators are the easiest way to create custom iterators
  • Generator expressions save memory (lazy evaluation)
  • itertools provides powerful, memory-efficient iteration tools
  • The 'in' operator on iterators is destructive (consumes elements)
""")

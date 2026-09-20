# A higher order function is a function that takes another function as a parameter
# They are called Higher order because they are functions of functions
# Examples
#   - Map #Map Object
#   - Reduce 
#   - Filter
# Lambda functions work great as a parameter to higher order functions if we can deal with their limitations
# Higher order functions operating on lists(sequences)
# Apply Function to every element
# map(function,iterables) 
n=int(input("Enter a number: "))
perfect_square=map(lambda x:x**2,range(1,n+1))
print(perfect_square)
perfect_square=list(map(lambda x:x**2,range(1,n+1)))
print(perfect_square)

add_one=lambda x:x+1
print(list(map(add_one,range(1,n+1))))

# ── map() with multiple iterables ──
# When multiple iterables are passed, map() applies the function element-wise
# map stops at the shortest iterable (like zip)
list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]
# Adds corresponding elements from list1 and list2
sum_of_two_lists = list(map(lambda x, y: x + y, list1, list2))
print(f"Sum of two lists: {sum_of_two_lists}")  # [11, 22, 33, 44, 55]

# Three iterables — multiply corresponding elements
list3 = [100, 200, 300, 400, 500]
product_of_three = list(map(lambda x, y, z: x * y * z, list1, list2, list3))
print(f"Product of three lists: {product_of_three}")  # [1000, 8000, 27000, 64000, 125000]

# Stops at shortest iterable
short_list = [1, 2]
long_list = [10, 20, 30, 40]
print(f"Shortest iterable wins: {list(map(lambda x, y: x + y, short_list, long_list))}")  # [11, 22]

# ── map() with built-in functions ──
# map() works with any callable — not just lambdas
numbers = [-3, -1, 0, 2, 5, -7]
# abs() returns absolute value
print(f"Absolute values: {list(map(abs, numbers))}")  # [3, 1, 0, 2, 5, 7]

# str() converts each element to string
print(f"To strings: {list(map(str, [1, 2, 3, 4]))}")  # ['1', '2', '3', '4']

# int() converts each element to integer
float_list = [1.5, 2.7, 3.1, 4.9]
print(f"Floats to ints (truncated): {list(map(int, float_list))}")  # [1, 2, 3, 4]

# float() converts each element to float
int_list = [1, 2, 3, 4]
print(f"Ints to floats: {list(map(float, int_list))}")  # [1.0, 2.0, 3.0, 4.0]

# len() on a list of strings
words = ["hello", "world", "python", "map"]
print(f"Lengths: {list(map(len, words))}")  # [5, 5, 6, 3]

# round() with map — rounding to 2 decimal places
decimals = [3.14159, 2.71828, 1.41421, 0.57721]
print(f"Rounded to 2 decimals: {list(map(lambda x: round(x, 2), decimals))}")  # [3.14, 2.72, 1.41, 0.58]

# ── map() with named (def) functions ──
def celsius_to_fahrenheit(c):
    """Converts Celsius to Fahrenheit: F = (C × 9/5) + 32"""
    return (c * 9/5) + 32

temperatures_c = [0, 20, 37, 100]
temperatures_f = list(map(celsius_to_fahrenheit, temperatures_c))
print(f"Celsius:    {temperatures_c}")
print(f"Fahrenheit: {temperatures_f}")  # [32.0, 68.0, 98.6, 212.0]

def is_even(n):
    """Returns True if n is even, False otherwise"""
    return n % 2 == 0

print(f"Even check: {list(map(is_even, range(1, 11)))}")
# [False, True, False, True, False, True, False, True, False, True]

# ── map() with strings ──
# Convert list of strings to uppercase
names = ["alice", "bob", "charlie", "diana"]
upper_names = list(map(str.upper, names))
print(f"Uppercase: {upper_names}")  # ['ALICE', 'BOB', 'CHARLIE', 'DIANA']

# Capitalize first letter
capitalized = list(map(str.capitalize, names))
print(f"Capitalized: {capitalized}")  # ['Alice', 'Bob', 'Charlie', 'Diana']

# Title case
titles = ["hello world", "python programming", "map function"]
print(f"Title case: {list(map(str.title, titles))}")  # ['Hello World', 'Python Programming', 'Map Function']

# Strip whitespace
messy_strings = ["  hello  ", " world ", "  python"]
print(f"Stripped: {list(map(str.strip, messy_strings))}")  # ['hello', 'world', 'python']

# Reverse each string using lambda + slicing
reversed_names = list(map(lambda s: s[::-1], names))
print(f"Reversed: {reversed_names}")  # ['ecila', 'bob', 'eilrahc', 'anaid']

# Get ASCII/Unicode values of characters in a string
print(f"ASCII codes of 'HELLO': {list(map(ord, 'HELLO'))}")  # [72, 69, 76, 76, 79]

# Convert ASCII codes back to characters
ascii_codes = [80, 121, 116, 104, 111, 110]
print(f"Chars from codes: {''.join(map(chr, ascii_codes))}")  # Python

# ── map() with dictionaries ──
# Extract values from a list of dictionaries
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78},
    {"name": "Diana", "grade": 95}
]
# Extract just the names
student_names = list(map(lambda s: s["name"], students))
print(f"Student names: {student_names}")  # ['Alice', 'Bob', 'Charlie', 'Diana']

# Extract grades and apply curve (+5)
# pyrefly: ignore [unsupported-operation]
curved_grades = list(map(lambda s: s["grade"] + 5, students))
print(f"Curved grades: {curved_grades}")  # [90, 97, 83, 100]

# Transform dictionaries — add a 'passed' field
passed_students = list(map(lambda s: {**s, "passed": int(s["grade"]) >= 80}, students))
for student in passed_students:
    print(f"  {student}")
# {'name': 'Alice', 'grade': 85, 'passed': True}
# {'name': 'Bob', 'grade': 92, 'passed': True}
# {'name': 'Charlie', 'grade': 78, 'passed': False}
# {'name': 'Diana', 'grade': 95, 'passed': True}

# ── map() vs list comprehension ──
# Both achieve the same result — map is functional style, list comp is Pythonic
# map()
squares_map = list(map(lambda x: x**2, range(1, 6)))
# list comprehension
squares_lc = [x**2 for x in range(1, 6)]
print(f"map():             {squares_map}")   # [1, 4, 9, 16, 25]
print(f"list comprehension: {squares_lc}")    # [1, 4, 9, 16, 25]

# Key differences:
# 1. map() returns a lazy iterator (memory efficient for large datasets)
# 2. List comprehension is generally more readable for simple cases
# 3. map() with a named function (no lambda) can be cleaner: map(str, list1)
# 4. List comprehension can filter (with if), map() cannot (use filter() for that)

# ── map() is lazy (returns an iterator) ──
# map() does NOT compute all values immediately — it's a lazy iterator
lazy_map = map(lambda x: x**3, [1, 2, 3, 4, 5])
print(f"map object: {lazy_map}")         # <map object at 0x...>
print(f"type: {type(lazy_map)}")          # <class 'map'>
# Values are computed on demand
print(f"next(): {next(lazy_map)}")        # 1
print(f"next(): {next(lazy_map)}")        # 8
print(f"remaining: {list(lazy_map)}")     # [27, 64, 125] — only unconsumed items

# ── map() with None (Python 2 behavior — NOT supported in Python 3) ──
# In Python 2, map(None, list1, list2) behaved like zip
# In Python 3, this raises TypeError: 'NoneType' object is not callable
# Use zip() instead:
zipped = list(zip([1, 2, 3], ['a', 'b', 'c']))
print(f"zip (replacement for map(None,...)): {zipped}")  # [(1, 'a'), (2, 'b'), (3, 'c')]

# ── Nested map() ──
# map() inside map() — apply transformation to a 2D list (matrix)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Double every element in the matrix
doubled_matrix = list(map(lambda row: list(map(lambda x: x * 2, row)), matrix))
print(f"Original matrix:  {matrix}")
print(f"Doubled matrix:   {doubled_matrix}")  # [[2, 4, 6], [8, 10, 12], [14, 16, 18]]

# Transpose a matrix using map and zip
transposed = list(map(list, zip(*matrix)))
print(f"Transposed matrix: {transposed}")  # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# ── Type conversion with map() ──
# Split a string of space-separated numbers and convert to integers
user_input = "10 20 30 40 50"
int_values = list(map(int, user_input.split()))
print(f"String '{user_input}' → integers: {int_values}")  # [10, 20, 30, 40, 50]

# Convert a list of booleans to integers (True→1, False→0)
bools = [True, False, True, True, False]
print(f"Bools to ints: {list(map(int, bools))}")  # [1, 0, 1, 1, 0]

# ── Practical example: format a table of data ──
products = [
    ("Laptop", 999.99, 5),
    ("Mouse", 29.50, 150),
    ("Keyboard", 74.99, 80),
    ("Monitor", 349.00, 20)
]
# Format each product as a readable string with total value
formatted = list(map(
    lambda p: f"  {p[0]:<10} | ${p[1]:>8.2f} | Qty: {p[2]:>3} | Total: ${p[1]*p[2]:>10.2f}",
    products
))
print("\n── Product Inventory ──")
print(f"  {'Product':<10} | {'Price':>8} | {'Qty':>5} | {'Total':>12}")
print(f"  {'-'*10}-+-{'-'*8}-+-{'-'*5}-+-{'-'*12}")
for line in formatted:
    print(line)

# ── Chaining map() calls ──
# Multiple transformations can be chained since map() returns an iterator
raw_data = ["  42  ", " 17 ", "  8  ", " 99 "]
# Chain: strip whitespace → convert to int → square
result = list(map(lambda x: x**2, map(int, map(str.strip, raw_data))))
print(f"\nChained map (strip → int → square): {result}")  # [1764, 289, 64, 9801]

# ── starmap() from itertools — for unpacking tuples ──
from itertools import starmap
# When each element is a tuple of arguments, use starmap instead of map
pairs = [(2, 5), (3, 3), (10, 2), (7, 4)]
powers = list(starmap(pow, pairs))
print(f"starmap(pow, pairs): {powers}")  # [32, 27, 100, 2401]

# starmap with lambda
points = [(1, 2), (3, 4), (5, 6)]
distances = list(starmap(lambda x, y: (x**2 + y**2)**0.5, points))
print(f"Distances from origin: {[round(d, 2) for d in distances]}")  # [2.24, 5.0, 7.81]

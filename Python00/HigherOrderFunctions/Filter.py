# ══════════════════════════════════════════════════════════════════════════════
# filter() — Higher-Order Function Tutorial
# ══════════════════════════════════════════════════════════════════════════════
# filter(function, iterable) → returns an iterator of elements for which
# the function returns True (truthy).
#
# Signature:  filter(function_or_None, iterable) → filter object
#   - function: a callable that accepts one argument and returns bool (truthy/falsy)
#   - iterable: any iterable (list, tuple, range, generator, string, …)
#
# Key characteristics:
#   1. Returns a lazy iterator (like map) — values computed on demand
#   2. Only KEEPS elements where function(element) is truthy
#   3. Does NOT transform elements — it selects them (use map() to transform)
#   4. If function is None, removes all falsy values (0, '', None, False, [], {})
# ══════════════════════════════════════════════════════════════════════════════

# ── Basic usage ──
# filter() with a lambda — keep only even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {evens}")  # [2, 4, 6, 8, 10]

# filter() returns a filter object (lazy iterator), not a list
raw_filter = filter(lambda x: x > 5, numbers)
print(f"filter object: {raw_filter}")        # <filter object at 0x...>
print(f"type: {type(raw_filter)}")            # <class 'filter'>
print(f"next(): {next(raw_filter)}")          # 6
print(f"next(): {next(raw_filter)}")          # 7
print(f"remaining: {list(raw_filter)}")       # [8, 9, 10] -- only unconsumed items

# ── filter() with named (def) functions ──
def is_positive(n):
    """Returns True if n is strictly positive"""
    return n > 0

mixed = [-5, -2, 0, 3, 7, -1, 10, -8]
positives = list(filter(is_positive, mixed))
print(f"\nPositive numbers: {positives}")  # [3, 7, 10]


def is_prime(n):
    """Returns True if n is a prime number (n >= 2)"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes_under_50 = list(filter(is_prime, range(50)))
print(f"Primes under 50: {primes_under_50}")
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

# ── filter() with None — remove falsy values ──
# When function is None, filter removes all falsy values
# Falsy values in Python: 0, 0.0, '', None, False, [], (), {}, set()
messy_data = [0, 1, "", "hello", None, True, False, [], [1, 2], {}, {"a": 1}, 0.0]
cleaned = list(filter(None, messy_data))
print(f"\nAfter removing falsy: {cleaned}")  # [1, 'hello', True, [1, 2], {'a': 1}]

# Practical use: clean up empty strings from user input
user_inputs = ["Alice", "", "Bob", "", "", "Charlie", ""]
valid_inputs = list(filter(None, user_inputs))
print(f"Valid inputs: {valid_inputs}")  # ['Alice', 'Bob', 'Charlie']

# ── filter() with numbers ──
# Keep numbers in a specific range
nums = list(range(1, 21))
between_5_and_15 = list(filter(lambda x: 5 <= x <= 15, nums))
print(f"\nBetween 5 and 15: {between_5_and_15}")  # [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Filter multiples of 3
multiples_of_3 = list(filter(lambda x: x % 3 == 0, range(1, 31)))
print(f"Multiples of 3 (1-30): {multiples_of_3}")  # [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

# Keep only perfect squares
import math
is_perfect_square = lambda n: math.isqrt(n) ** 2 == n
perfect_squares = list(filter(is_perfect_square, range(1, 101)))
print(f"Perfect squares (1-100): {perfect_squares}")  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Filter out outliers (keep values within 2 standard deviations)
import statistics
data = [10, 12, 11, 13, 100, 12, 11, 14, 10, -50, 13, 11]
mean = statistics.mean(data)
stdev = statistics.stdev(data)
within_bounds = list(filter(lambda x: abs(x - mean) <= 2 * stdev, data))
print(f"Data: {data}")
print(f"Mean: {mean:.1f}, Stdev: {stdev:.1f}")
print(f"Without outliers: {within_bounds}")

# ── filter() with strings ──
# Keep strings longer than 3 characters
words = ["hi", "hello", "hey", "greetings", "yo", "howdy", "ok"]
long_words = list(filter(lambda w: len(w) > 3, words))
print(f"\nWords longer than 3 chars: {long_words}")  # ['hello', 'greetings', 'howdy']

# Filter strings that start with a specific letter
names = ["Alice", "Bob", "Anna", "Charlie", "Alex", "Diana", "Amy"]
a_names = list(filter(lambda s: s.startswith("A"), names))
print(f"Names starting with 'A': {a_names}")  # ['Alice', 'Anna', 'Alex', 'Amy']

# Keep only alphabetic strings (no numbers, no special chars)
mixed_strings = ["hello", "world123", "python", "42", "foo_bar", "AI", "!!!", "data"]
alpha_only = list(filter(str.isalpha, mixed_strings))
print(f"Alpha only: {alpha_only}")  # ['hello', 'python', 'AI', 'data']

# Keep only strings that are valid integers
candidates = ["42", "hello", "100", "3.14", "-7", "abc", "0"]
valid_ints = list(filter(lambda s: s.lstrip("-").isdigit(), candidates))
print(f"Valid integers: {valid_ints}")  # ['42', '100', '-7', '0']

# Filter palindromes
words_list = ["racecar", "hello", "madam", "python", "level", "world", "radar", "kayak"]
palindromes = list(filter(lambda w: w == w[::-1], words_list))
print(f"Palindromes: {palindromes}")  # ['racecar', 'madam', 'level', 'radar', 'kayak']

# Filter strings containing a vowel
has_vowel = lambda s: any(c in "aeiouAEIOU" for c in s)
test_strings = ["rhythm", "hello", "gym", "crypt", "python", "sky", "myth"]
with_vowels = list(filter(has_vowel, test_strings))
print(f"Contains vowels: {with_vowels}")  # ['hello', 'python']

# ── filter() with dictionaries (list of dicts) ──
students = [
    {"name": "Alice", "grade": 85, "age": 20},
    {"name": "Bob", "grade": 92, "age": 22},
    {"name": "Charlie", "grade": 58, "age": 19},
    {"name": "Diana", "grade": 95, "age": 21},
    {"name": "Eve", "grade": 73, "age": 23},
    {"name": "Frank", "grade": 41, "age": 20},
]

# Keep students who passed (grade >= 60)
# pyrefly: ignore [unsupported-operation]
passed = list(filter(lambda s: s["grade"] >= 60, students))
print(f"\nPassed students:")
for s in passed:
    print(f"  {s['name']}: {s['grade']}")
# Alice: 85, Bob: 92, Diana: 95, Eve: 73

# Honor roll (grade >= 90)
# pyrefly: ignore [unsupported-operation]
honor_roll = list(filter(lambda s: s["grade"] >= 90, students))
print(f"Honor roll: {[s['name'] for s in honor_roll]}")  # ['Bob', 'Diana']

# Students aged 20 or under
# pyrefly: ignore [unsupported-operation]
young_students = list(filter(lambda s: s["age"] <= 20, students))
print(f"Age <= 20: {[s['name'] for s in young_students]}")  # ['Alice', 'Charlie', 'Frank']

# ── filter() with tuples ──
# Filter products by price range
products = [
    ("Laptop", 999.99),
    ("Mouse", 29.50),
    ("Keyboard", 74.99),
    ("Monitor", 349.00),
    ("USB Cable", 9.99),
    ("Headset", 59.99),
    ("Webcam", 44.95),
]
affordable = list(filter(lambda p: p[1] < 100, products))
print(f"\nProducts under $100:")
for name, price in affordable:
    print(f"  {name}: ${price:.2f}")

# ── filter() vs list comprehension ──
# Both achieve the same result — filter is functional, list comp is Pythonic
numbers = list(range(1, 21))

# Using filter
evens_filter = list(filter(lambda x: x % 2 == 0, numbers))

# Using list comprehension
evens_lc = [x for x in numbers if x % 2 == 0]

print(f"\nfilter():           {evens_filter}")
print(f"list comprehension: {evens_lc}")
# Both produce: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Key differences:
# 1. filter() returns a lazy iterator (memory efficient for large datasets)
# 2. List comprehension can filter AND transform in one expression
# 3. filter() with a named function (no lambda) is very clean: filter(is_prime, nums)
# 4. List comprehension is generally considered more Pythonic
# 5. filter() can use None to remove falsy values — no easy list comp equivalent

# When filter() wins — clean and readable with a named function:
#   filter(is_prime, range(1000))
# When list comp wins — filtering + transformation in one step:
#   [x**2 for x in range(1000) if is_prime(x)]

# ── filterfalse() from itertools — the inverse of filter() ──
from itertools import filterfalse

# filterfalse keeps elements where the function returns FALSE (opposite of filter)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odds_via_filterfalse = list(filterfalse(lambda x: x % 2 == 0, numbers))
print(f"\nfilterfalse (NOT even -> odds): {odds_via_filterfalse}")  # [1, 3, 5, 7, 9]

# Partition a list into two groups using filter + filterfalse
def partition(predicate, iterable):
    """Splits iterable into (truthy, falsy) based on predicate"""
    items = list(iterable)  # materialize to iterate twice
    return list(filter(predicate, items)), list(filterfalse(predicate, items))

passes, fails = partition(lambda s: int(s["grade"]) >= 60, students)
print(f"Passed: {[s['name'] for s in passes]}")   # ['Alice', 'Bob', 'Diana', 'Eve']
print(f"Failed: {[s['name'] for s in fails]}")     # ['Charlie', 'Frank']

# ── Chaining filter() with map() ──
# filter selects, map transforms — they compose naturally
# Example: Get uppercase names of students who passed
# pyrefly: ignore [unsupported-operation]
honor_names = list(map(
    lambda s: s["name"].upper(),
    filter(lambda s: s["grade"] >= 90, students)
))
print(f"\nHonor roll (uppercase): {honor_names}")  # ['BOB', 'DIANA']

# Chain: filter valid numbers → convert to int → filter even → square
raw_data = ["42", "hello", "7", "not_a_number", "18", "3", "100", "xyz"]
result = list(
    map(
        lambda x: x ** 2,                     # 3. square them
        filter(
            lambda x: x % 2 == 0,             # 2. keep even
            map(int,                           # 1. convert to int
                filter(str.isdigit, raw_data)  # 0. keep digit strings only
            )
        )
    )
)
print(f"Chained (filter -> int -> even -> square): {result}")  # [1764, 324, 10000]

# The same thing with a list comprehension (arguably more readable for complex chains):
result_lc = [int(x)**2 for x in raw_data if x.isdigit() and int(x) % 2 == 0]
print(f"Same with list comp: {result_lc}")  # [1764, 324, 10000]

# ── filter() with strings (filtering characters) ──
# A string is an iterable of characters — filter works on individual chars
sentence = "Hello, World! Python 3.12 is awesome."

# Keep only alphabetic characters
letters_only = "".join(filter(str.isalpha, sentence))
print(f"\nLetters only: {letters_only}")  # HelloWorldPythonisawesome

# Keep only digits
digits_only = "".join(filter(str.isdigit, sentence))
print(f"Digits only: {digits_only}")  # 312

# Remove vowels from a string
consonants = "".join(filter(lambda c: c.lower() not in "aeiou", sentence))
print(f"Without vowels: {consonants}")  # Hll, Wrld! Pythn 3.12 s wsm.

# Keep only printable non-whitespace characters
import string
visible = "".join(filter(lambda c: c in string.printable and c not in string.whitespace, sentence))
print(f"Visible chars: {visible}")  # Hello,World!Python3.12isawesome.

# ── filter() with sets and generators ──
# filter works with any iterable, not just lists
# With a set
unique_nums = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_set = set(filter(lambda x: x % 2 == 0, unique_nums))
print(f"\nEven from set: {sorted(even_set)}")  # [2, 4, 6, 8, 10]

# With a generator (fully lazy pipeline — nothing computed until consumed)
def infinite_counter(start=1):
    """Generates integers starting from 'start' indefinitely"""
    n = start
    while True:
        yield n
        n += 1

# First 10 even numbers from an infinite generator (lazy!)
from itertools import islice
first_10_evens = list(islice(filter(lambda x: x % 2 == 0, infinite_counter()), 10))
print(f"First 10 evens (from infinite gen): {first_10_evens}")
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# ── Practical example: Log file analysis ──
log_lines = [
    "2024-01-15 08:23:01 INFO  Server started on port 8080",
    "2024-01-15 08:23:45 DEBUG Database connection pool initialized",
    "2024-01-15 08:24:12 ERROR Failed to load configuration file",
    "2024-01-15 08:25:00 INFO  User 'admin' logged in",
    "2024-01-15 08:25:33 WARNING Disk usage above 85%",
    "2024-01-15 08:26:01 ERROR Connection timeout after 30s",
    "2024-01-15 08:26:45 INFO  Scheduled backup started",
    "2024-01-15 08:27:10 DEBUG Cache hit ratio: 94%",
    "2024-01-15 08:28:00 WARNING Memory usage above 90%",
    "2024-01-15 08:28:30 ERROR Out of memory exception in worker thread",
]

# Filter only ERROR lines
errors = list(filter(lambda line: "ERROR" in line, log_lines))
print("\n-- Log Analysis --")
print(f"Total log lines: {len(log_lines)}")
print(f"Errors found: {len(errors)}")
for e in errors:
    print(f"  [ERROR] {e}")

# Filter WARNING and ERROR
critical = list(filter(lambda line: "WARNING" in line or "ERROR" in line, log_lines))
print(f"Critical issues: {len(critical)}")

# ── Practical example: Data validation ──
emails = [
    "alice@example.com",
    "bob@",
    "charlie@company.org",
    "invalid-email",
    "diana@school.edu",
    "@missing-name.com",
    "eve@domain.co.uk",
    "",
    "frank@.com",
]

def is_valid_email(email):
    """Basic email validation — checks structure, not full RFC 5322 compliance"""
    if not email or "@" not in email:
        return False
    local, _, domain = email.partition("@")
    if not local or not domain:
        return False
    if "." not in domain:
        return False
    if domain.startswith(".") or domain.endswith("."):
        return False
    return True

valid_emails = list(filter(is_valid_email, emails))
invalid_emails = list(filterfalse(is_valid_email, emails))

print("\n-- Email Validation --")
print(f"Valid emails:")
for e in valid_emails:
    print(f"  [OK] {e}")
print(f"Invalid emails:")
for e in invalid_emails:
    print(f"  [INVALID] {repr(e)}")

# ── Practical example: File extension filtering ──
filenames = [
    "report.pdf", "data.csv", "image.png", "script.py",
    "notes.txt", "photo.jpg", "app.js", "style.css",
    "readme.md", "archive.zip", "model.py", "test.py",
]

# Filter Python files
python_files = list(filter(lambda f: f.endswith(".py"), filenames))
print(f"\nPython files: {python_files}")  # ['script.py', 'model.py', 'test.py']

# Filter image files
image_extensions = (".png", ".jpg", ".jpeg", ".gif", ".bmp", ".svg")
images = list(filter(lambda f: f.endswith(image_extensions), filenames))
print(f"Image files: {images}")  # ['image.png', 'photo.jpg']

# ── Practical example: Inventory management ──
inventory = [
    {"item": "Laptop",     "qty": 15, "price": 999.99, "category": "Electronics"},
    {"item": "Mouse",      "qty": 0,  "price": 29.50,  "category": "Electronics"},
    {"item": "Notebook",   "qty": 200,"price": 4.99,   "category": "Office"},
    {"item": "Pen",        "qty": 500,"price": 1.50,   "category": "Office"},
    {"item": "Monitor",    "qty": 3,  "price": 349.00, "category": "Electronics"},
    {"item": "Stapler",    "qty": 0,  "price": 12.99,  "category": "Office"},
    {"item": "Webcam",     "qty": 25, "price": 44.95,  "category": "Electronics"},
    {"item": "Paper Ream", "qty": 0,  "price": 8.99,   "category": "Office"},
]

# Items that need restocking (qty == 0)
out_of_stock = list(filter(lambda p: int(p["qty"]) == 0, inventory))
print("\n-- Inventory Report --")
print("Out of stock:")
for item in out_of_stock:
    print(f"  [!] {item['item']} (${item['price']:.2f})")

# High-value electronics in stock
# pyrefly: ignore [unsupported-operation]
high_value_electronics = list(filter(
    lambda p: p["category"] == "Electronics" and p["qty"] > 0 and p["price"] > 100,
    inventory
))
print("High-value electronics in stock:")
for item in high_value_electronics:
    print(f"  [$] {item['item']}: {item['qty']} units @ ${item['price']:.2f}")

# ── filter() with enumerate — filter by index ──
# Sometimes you need the index to decide what to keep
items = ["zero", "one", "two", "three", "four", "five", "six", "seven"]

# Keep elements at even indices
even_indexed = [val for idx, val in enumerate(items) if idx % 2 == 0]
print(f"\nEven-indexed items: {even_indexed}")  # ['zero', 'two', 'four', 'six']

# Using filter with enumerate (functional style)
even_indexed_f = list(map(
    lambda pair: pair[1],
    filter(lambda pair: pair[0] % 2 == 0, enumerate(items))
))
print(f"Same via filter+enumerate: {even_indexed_f}")

# ── compress() from itertools — filter by selector mask ──
from itertools import compress

# compress returns elements where the corresponding selector is True
data = ["A", "B", "C", "D", "E", "F"]
selectors = [True, False, True, True, False, True]
selected = list(compress(data, selectors))
print(f"\ncompress() with mask: {selected}")  # ['A', 'C', 'D', 'F']

# Practical use: filter columns of data
headers = ["Name", "Age", "Email", "Phone", "Address"]
show_columns = [True, True, True, False, False]  # only show Name, Age, Email
visible_headers = list(compress(headers, show_columns))
print(f"Visible columns: {visible_headers}")  # ['Name', 'Age', 'Email']

# ── takewhile() and dropwhile() from itertools ──
from itertools import takewhile, dropwhile

sorted_nums = [2, 4, 6, 8, 3, 5, 7, 10, 12]

# takewhile: take elements while condition is True, stop at first False
taken = list(takewhile(lambda x: x % 2 == 0, sorted_nums))
print(f"\ntakewhile(even): {taken}")  # [2, 4, 6, 8] -- stops at 3

# dropwhile: skip elements while condition is True, keep the rest
dropped = list(dropwhile(lambda x: x % 2 == 0, sorted_nums))
print(f"dropwhile(even): {dropped}")  # [3, 5, 7, 10, 12] -- starts from 3

# Practical use: skip header lines
csv_lines = [
    "# This is a comment",
    "# Generated on 2024-01-15",
    "# Format: name,age,grade",
    "Alice,20,85",
    "Bob,22,92",
    "Charlie,19,78",
]
data_lines = list(dropwhile(lambda line: line.startswith("#"), csv_lines))
print(f"Data lines (skipped headers): {data_lines}")

# ── Summary: filter() vs related tools ──
# ┌─────────────────────────┬─────────────────────────────────────────────────┐
# │ Tool                    │ Use Case                                        │
# ├─────────────────────────┼─────────────────────────────────────────────────┤
# │ filter(func, iter)      │ Keep elements where func returns True           │
# │ filter(None, iter)      │ Remove all falsy values (0, '', None, False...) │
# │ filterfalse(func, iter) │ Keep elements where func returns False          │
# │ takewhile(func, iter)   │ Take from start until func returns False        │
# │ dropwhile(func, iter)   │ Skip from start until func returns False        │
# │ compress(data, selectors│ Keep elements where selector is True (mask)     │
# │ [x for x in i if cond]  │ List comp — filter + optional transform         │
# │ map(func, iter)         │ Transform elements (does NOT filter)            │
# └─────────────────────────┴─────────────────────────────────────────────────┘

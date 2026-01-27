# 🔷 Type Conversion & Type Casting in Python
# 1️⃣ What is Type Conversion?
# Type conversion means changing one data type into another.

# Python has two types:
# Implicit Type Conversion (automatic)
# Explicit Type Conversion (Type Casting) (manual)

# | Task            | JavaScript     | Python      |
# | --------------- | -------------- | ----------- |
# | String → Number | `Number("10")` | `int("10")` |
# | Number → String | `String(10)`   | `str(10)`   |
# | Boolean         | `Boolean()`    | `bool()`    |

# 🔹 1. Implicit Type Conversion (Automatic)
# Python automatically converts lower type → higher type.

# Example:
a = 10        # int
b = 2.5       # float
c = a + b
print(c)      # 12.5
print(type(c))

# ✔ int converted to float automatically
# ✔ No data loss
# 📌 JS behaves similarly here


# 2. Explicit Type Conversion (Type Casting)
# Programmer manually converts data type using functions.
# Common Type Casting Functions
# | Function  | Converts To |
# | --------- | ----------- |
# | `int()`   | Integer     |
# | `float()` | Float       |
# | `str()`   | String      |
# | `bool()`  | Boolean     |
# | `list()`  | List        |
# | `tuple()` | Tuple       |
# | `set()`   | Set         |


# 1️⃣ String → Integer
age = "22"
age = int(age)

print(age)
print(type(age))
# ⚠ String must contain only numbers

# 2️⃣ Integer → Float
a = 10
b = float(a)

print(b)   # 10.0

# 3️⃣ Number → String
marks = 85
marks = str(marks)

print(marks)
print(type(marks))
# (JS equivalent → String(marks))

# 4️⃣ User Input Type Conversion (Very Important)
# By default, input is string.

a = input("Enter number: ")
b = input("Enter number: ")

print(a + b)   # string concatenation

# Correct way:
a = int(input("Enter number: "))
b = int(input("Enter number: "))

print(a + b)

# 5️⃣ Boolean Type Conversion
print(bool(0))      # False
print(bool(1))      # True
print(bool(""))     # False
print(bool("Hi"))   # True
# 📌 Empty values → False
# 📌 Non-empty → True

# 6️⃣ List, Tuple, Set Conversion
nums = [1, 2, 3]

print(tuple(nums))  # (1, 2, 3)
print(set(nums))    # {1, 2, 3}

# 7️⃣ Float → Integer (Data Loss)
x = 10.9
y = int(x)

print(y)   # 10
# ⚠ Decimal part is removed

# 🔷 Type Conversion & Type Casting (with dict())
# 1️⃣ dict() Type Conversion
# The dict() function is used to convert certain data types into a dictionary.

# 📌 Important rule
# The data must be in key–value pair format.

# 2️⃣ List → Dictionary
# Example (List of Tuples)
data = [("name", "Sagar"), ("age", 22), ("course", "CSIT")]

student = dict(data)

print(student)

# Output:
# {'name': 'Sagar', 'age': 22, 'course': 'CSIT'}

# ✔ Each item must be a pair (2 values)

# 3️⃣ Tuple → Dictionary
data = (("a", 1), ("b", 2), ("c", 3))

result = dict(data)

print(result)


# Output:
# {'a': 1, 'b': 2, 'c': 3}

# 4️⃣ Dictionary Copy Using dict()
user1 = {"name": "Ram", "age": 20}

user2 = dict(user1)

print(user2)


# ✔ Creates a new dictionary

# 5️⃣ Two Lists → Dictionary using zip()
keys = ["name", "age", "course"]
values = ["Sagar", 22, "CSIT"]

student = dict(zip(keys, values))

print(student)


# Output:
# {'name': 'Sagar', 'age': 22, 'course': 'CSIT'}


# 📌 Very important for exams & interviews

# 6️⃣ Invalid dict() Conversion (Common Mistake ❌)
data = ["a", "b", "c"]
dict(data)
# ❌ Error because key–value pair is missing

# 7️⃣ String → Dictionary ❌
data = "abc"
dict(data)


# # ❌ Not possible directly
# 🔑 Quick Summary (Exam Points)

# ✔ dict() converts pair-based data into dictionary
# ✔ Each element must have exactly two values
# ✔ zip() is commonly used with dict()
# ✔ Not all data types can be converted to dictionary
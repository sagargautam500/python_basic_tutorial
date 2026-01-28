# 🔷 What is a Lambda Function?
# A lambda function is:
# A small, anonymous function (no name)
# Written in one line
# Used for short operations
# 📌 Think of it as quick function.

# 🔷 Syntax of Lambda Function
# lambda arguments : expression
# ⚠ Rules:
# Only one expression
# Expression is automatically returned
# No return keyword
# No multiple statements

# 🔹 Normal Function vs Lambda
# Normal Function (Python)
def add(a, b):
    return a + b
# Lambda Function
add = lambda a, b: a + b
# ✔ Same work
# ✔ Less code

# Example 3: Check even or odd
is_even = lambda x: x % 2 == 0
print(is_even(6))


# 🔷 Lambda with Built-in Functions (VERY IMPORTANT 🔥)
# 1️⃣ map()
# Python
nums = [1, 2, 3, 4]

result = list(map(lambda x: x * 2, nums))
print(result)

# 🟢 Doubles each element
# JS Equivalent
# let nums = [1, 2, 3, 4];
# let result = nums.map(x => x * 2);

# 2️⃣ filter()
# Python
nums = [1, 2, 3, 4, 5]
result = list(filter(lambda x: x % 2 == 0, nums))
print(result)

# 🟢 Filters even numbers
# JS Equivalent
# let nums = [1, 2, 3, 4, 5];
# let result = nums.filter(x => x % 2 === 0);

# 3️⃣ reduce() (from functools)
# Python
from functools import reduce

nums = [1, 2, 3, 4]

result = reduce(lambda a, b: a + b, nums)
print(result)

# JS Equivalent
# let nums = [1, 2, 3, 4];
# let result = nums.reduce((a, b) => a + b);

# 🔷 Lambda vs Normal Function
# | Feature     | Lambda | Normal Function |
# | ----------- | ------ | --------------- |
# | Name        | ❌ No   | ✅ Yes           |
# | Lines       | 1      | Multiple        |
# | Complexity  | Simple | Any             |
# | Reusability | Low    | High            |
# | Readability | Medium | High            |


# 🔷 When to Use Lambda?
# ✔ Short logic
# ✔ One-time use
# ✔ Inside map, filter, reduce
# ✔ Cleaner code
# ❌ Avoid for complex logic

# 🔑 Final One-Line Summary
# Lambda function = small, anonymous, one-line function for quick tasks
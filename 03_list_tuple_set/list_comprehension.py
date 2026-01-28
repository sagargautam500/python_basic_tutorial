# 🔷 What is List Comprehension? (Simple Meaning)
# List comprehension is a short and clean way to create a new list using a loop and condition in ONE line.

# 📌 It replaces:
# for loop
# if condition
# append()

# ❌ Normal Way (Without List Comprehension)
# Let’s start slow.
# Task:
# 👉 From a list, double the even numbers and store them.

nums = [1, 2, 3, 4, 5]
result = []

for x in nums:
    if x % 3 == 0:
        result.append(x * 2)

print(result)

# ✅ Same Task Using List Comprehension (Pythonic Way ⭐)
nums = [1, 2, 3, 4, 5]

result = [x * 2 for x in nums if x % 3 == 0]
print(result)
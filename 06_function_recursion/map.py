# 🔷 What is map()?
# Simple definition 👇
# map() applies a function to every element of a list (or iterable).
# 📌 Think:
# “Take each item → do something → return new list”

# 🟢 Python map() — EASY WAY
# 🔹 Syntax
# map(function, iterable)
# function → what to do with each item
# iterable → list, tuple, etc.
# ⚠ map() returns a map object, so we usually convert it to list.

#example
nums = [1, 2, 3, 4]

result = list(map(lambda x: x * 2, nums))
print(result)
# ✔ Less code
# ✔ Cleaner
# ✔ Faster

# 🟡 JavaScript map()
# let nums = [1, 2, 3, 4];

# let result = nums.map(x => x * 2);
# console.log(result);

# 🔑 Use map() when:
# ✔ You want to modify every element
# ✔ Length of list remains same
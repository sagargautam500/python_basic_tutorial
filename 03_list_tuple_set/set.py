# 🔷 Set in Python
# 1️⃣ What is a Set?
# A set is a collection of unique elements that is:
# Unordered
# No duplicate values
# Mutable
#Each element must be immutable (like numbers, strings, tuples)

s = {1, 2, 3}

# 2️⃣ Creating a Set
nums = {1, 2, 3, 4}

# Duplicate values removed automatically
nums = {1, 2, 2, 3}
print(nums)   # {1, 2, 3}

# 3️⃣ Empty Set (Very Important ⚠️)
s = {}        # ❌ dictionary
s = set()     # ✅ empty set


# 5️⃣ Accessing Set Elements
# ❌ Cannot use indexing

s = {1, 2, 3}
# print(s[0]) ❌ Error

# ✔ Use loop

for i in s:
    print(i)


# 6️⃣ Adding Elements
s = {1, 2}

s.add(3)
print(s)

# Add multiple elements
s.update([4, 5, 6])


# 7️⃣ Removing Elements
s.remove(2)     # error if not found
s.discard(5)    # no error
s.pop()         # removes random element
s.clear()       # remove all

# 8️⃣ Set Methods (Important)
# | Method      | Work           |
# | ----------- | -------------- |
# | `add()`     | Add element    |
# | `update()`  | Add many       |
# | `remove()`  | Remove element |
# | `discard()` | Remove safely  |
# | `pop()`     | Remove random  |
# | `clear()`   | Empty set      |


# 9️⃣ Set Operations (Very Important 🔥)
# Union
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)
print(a.union(b))

# Intersection
print(a & b)
print(a.intersection(b))

# Difference
print(a - b)
print(a.difference(b))

# Symmetric Difference
print(a ^ b)
print(a.symmetric_difference(b))


# 🔟 Membership Test
s = {1, 2, 3}
print(2 in s)   # True

# 1️⃣1️⃣ Convert Other Types to Set
lst = [1, 2, 2, 3]
print(set(lst))   # {1, 2, 3}
# 📌 Used to remove duplicates

# 1️⃣2️⃣ Frozen Set (Immutable Set)
fs = frozenset([1, 2, 3])
# ❌ Cannot add or remove elements

# | JavaScript | Python     |
# | ---------- | ---------- |
# | `Set()`    | `set()`    |
# | `add()`    | `add()`    |
# | `has()`    | `in`       |
# | `delete()` | `remove()` |

# let s = new Set([1, 2, 2, 3]); #in js

# 🔑 Exam Important Points

# ✔ Set stores unique values
# ✔ Unordered, no indexing
# ✔ Best for removing duplicates
# ✔ Supports mathematical operations
# ✔ set() ≠ {}
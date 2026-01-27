# 🔷 Tuple in Python
# 1️⃣ What is a Tuple?
# A tuple is a collection of ordered elements that is immutable (cannot be changed).

t = (1, 2, 3)

# 2️⃣ Creating Tuple
# Normal Tuple
nums = (1, 2, 3)

# Tuple without parentheses
nums = 1, 2, 3

# Single-element Tuple (Very Important ⚠️)
t = (5,)   # correct
# ❌ (5) is not a tuple

# 3️⃣ Tuple vs List (Key Difference)
# List	         Tuple
# Mutable	    Immutable
# Uses []	    Uses ()
# More memory	Less memory
# Slower	    Faster


# 4️⃣ Accessing Tuple Elements (Indexing)
t = (10, 20, 30)

print(t[0])   # 10
print(t[-1])  # 30
# ✔ Index starts from 0
# ✔ Negative indexing allowed

# 5️⃣ Tuple Slicing
t = (1, 2, 3, 4, 5)
print(t[1:4])   # (2, 3, 4)

# 6️⃣ Tuple is Immutable ❌
t = (1, 2, 3)
t[0] = 10    # ❌ Error
# ✔ Values cannot be changed

# 7️⃣ Loop Through Tuple
t = ("a", "b", "c")

for item in t:
    print(item)


# 8️⃣ Tuple Methods (Very Few)
# 1️⃣ count()
t = (1, 2, 2, 3)
print(t.count(2))   # 2

# 2️⃣ index()
print(t.index(3))   # 3
# 📌 Tuples have only 2 methods

# 9️⃣ Tuple Packing & Unpacking (Important 🔥)
# Packing
data = ("Sagar", 22, "CSIT")

# Unpacking
name, age, course = data

print(name)
print(age)
print(course)

# 🔟 Tuple with Mixed Data
t = (1, "Python", 3.5, True)


# 1️⃣1️⃣ Tuple inside List / List inside Tuple
t = (1, [2, 3], 4)
t[1][0] = 99   # allowed
# ✔ Tuple is immutable
# ✔ But mutable objects inside tuple can change

# 1️⃣2️⃣ Convert Tuple ↔ List
t = (1, 2, 3)
lst = list(t)

lst.append(4)
t = tuple(lst)

# 🔷 Tuple vs JavaScript
# JavaScript        	     Python
# No tuple	                Tuple exists
# Arrays are mutable	    Tuple is immutable
# Object.freeze() needed	Built-in immutability

# 🔑 Exam Important Points
# ✔ Tuples are immutable
# ✔ Faster than list
# ✔ Used for fixed data
# ✔ Only count() and index() methods
# ✔ Single-element tuple needs comma
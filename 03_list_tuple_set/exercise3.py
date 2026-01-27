# Let‘s Practice
# Figure out a way to store 9 & 9.0 as separate values in the set. (You can take help of built-in data types) 
# In Python:

9 == 9.0   # True
# So a set treats them as same value and stores only one.

# ✅ Way to store 9 & 9.0 as separate values in a set
# ✔️ Using different data types (recommended)
my_set = {9, "9.0"}
print(my_set)

# 👉 Here:
# 9 → integer
# "9.0" → string
# So Python treats them as different values.

# ✔️ Another correct way (using tuple + type)
my_set = {(9, int), (9.0, float)}
print(my_set)

# ❌ Why this does NOT work
my_set = {9, 9.0}   # ❌
# Because Python considers them equal.


# 🧠 Key Concept
# Sets store unique values, and 9 & 9.0 are equal in Python unless their types differ.
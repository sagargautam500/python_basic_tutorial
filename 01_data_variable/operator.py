# 🔷 Operators in Python
# Operators are used to perform operations on variables and values.

# 1️⃣ Arithmetic Operators
# Operator	Meaning	         Example
# +	        Addition	     a + b
# -	       Subtraction	     a - b
# *	      Multiplication	 a * b
# /	        Division	     a / b
# %	         Modulus	     a % b
# **	      Power	         a ** b
# //	  Floor division	 a // b

# 📌 ** and // are extra in Python (not in JS)
# Example:
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.33
print(a % b)   # 1
print(a ** b)  # 1000
print(a // b)  # 3


# 2️⃣ Comparison (Relational) Operators
# Used to compare values → result is True or False.

# Operator   	Meaning
# ==	       Equal to
# !=	       Not equal
# >	          Greater than
# <	           Less than
# >=	    Greater than or equal
# <=	    Less than or equal

# Example:
a = 10
b = 5

print(a == b)   # False
print(a != b)   # True
print(a > b)    # True
print(a <= b)   # False


# 3️⃣ Assignment Operators
# Used to assign values.
# Operator	 Example	Same as
# =	         a = 5	    Assign
# +=	     a += 3	   a = a + 3
# -=	     a -= 2	   a = a - 2
# *=	     a *= 2	   a = a * 2
# /=	     a /= 2	   a = a / 2

# Example:
a = 10
a += 5
print(a)   # 15


# 4️⃣ Logical Operators
# Used with conditions.
# Operator	  Meaning
# and	    Both true
# or	    At least one true
# not	    Reverse result

# Example:
a = 10
b = 5

print(a > 5 and b < 10)   # True
print(a < 5 or b < 10)    # True
print(not(a > 5))         # False

# 📌 JS uses &&, ||, !
# 📌 Python uses words

# 5️⃣ Membership Operators
# Check if value exists in a sequence.

# Operator	 Meaning
# in	     Exists
# not in	 Does not exist

# Example:
nums = [1, 2, 3]

print(2 in nums)      # True
print(5 not in nums) # True

# 6️⃣ Identity Operators
# Check same memory location.

# Operator	 Meaning
# is	    Same object
# is not	Different object

# Example:
a = 10
b = 10

print(a is b)       # True
print(a is not b)   # False
# (JS equivalent → === checks value & type, not memory)


# 7️⃣ Bitwise Operators (Basic)
# Operator	 Meaning
# &	          AND
# `	            `
# ^           XOR
# ~	          NOT
# <<	   Left shift
# >>	   Right shift

# Example:
a = 5
b = 3

print(a & b)  # 1
print(a | b)  # 7
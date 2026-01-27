# 🔷 Conditional Statements
# Conditional statements are used to make decisions based on conditions.

# JavaScript
# let age = 18;
# if (age >= 18) {
#   console.log("Adult");
# }

# python
age=18
if age>=18:
    print("adult age")

# 🔑 Difference
# JS uses { }
# Python uses indentation
# Python uses : after condition


# 2️⃣ if – else Statement
# JavaScript
# let num = 5;
# if (num % 2 === 0) {
#   console.log("Even");
# } else {
#   console.log("Odd");
# }

# python
num=5
if num % 2 == 0:
    print("Even")
else:
    print("odd")


# 3️⃣ if – else if – else (elif in Python)
# JavaScript
# let marks = 75;

# if (marks >= 80) {
#   console.log("Distinction");
# } else if (marks >= 60) {
#   console.log("First Division");
# } else {
#   console.log("Fail");
# }

# python
marks=75

if marks >= 80:
    print("Disction")
elif marks >= 60:
    print("first division")
else:
    print("fail")
    
# 🔑 Key Difference
# JavaScript	Python
# else if    	elif


# 4️⃣ Nested if Statement
# JavaScript
# let age = 20;
# let hasId = true;

# if (age >= 18) {
#   if (hasId) {
#     console.log("Allowed");
#   }
# }

# python
age=20
has_id=True

if age >= 18:
    if has_id:
        print("allowed")



# 5️⃣ Logical Operators in Conditions
# JavaScript	Python
# &&	         and
# ||	          or
# !	             not

# JavaScript
# if (age >= 18 && hasId) {
#   console.log("Allowed");
# }

# python
if age >=18 and has_id:
    print("allowed")

# 6️⃣ Ternary Operator (One-Line Condition)
# JavaScript
# let result = age >= 18 ? "Adult" : "Minor";

# Python
result = "Adult" if age >= 18 else "Minor"


# 7️⃣ Multiple Conditions
# JavaScript
# if (age >= 18 && age <= 60) {
#   console.log("Working age");
# }

# Python
if 18 <= age <= 60:
    print("Working age")

# 🔥 Python supports chained comparison

# ✅ Final Summary (Exam Points)

# ✔ if, elif, else control decision making
# ✔ Python uses indentation, JS uses braces
# ✔ elif = else if
# ✔ Python supports chained conditions

# 🔁 What is Recursion? (Very Easy Definition)
# Recursion is a function calling itself to solve a problem.
# 📌 Used when a problem can be broken into smaller same problems.

# 🧠 Real-Life Example
# 📦 Boxes inside boxes
# To open big box → open smaller box
# Same action repeated
# That’s recursion.

# 🔷 Two MOST IMPORTANT Parts of Recursion

# Every recursive function MUST have:
# 1️⃣ Base Case → when to stop
# 2️⃣ Recursive Case → function calls itself
# ⚠ Without base case → infinite loop / stack overflow

# 🔹 Simple Recursion Example (Countdown)
def countdown(n):
    if n == 0:          # base case
        return
    print(n)
    countdown(n - 1)    # recursive call

countdown(5)
# 🔍 How It Works (Step-by-step)
# countdown(5)
#  → print 5 → countdown(4)
#  → print 4 → countdown(3)
#  → print 3 → countdown(2)
#  → print 2 → countdown(1)
#  → print 1 → countdown(0)
#  → stop

#example 2:Factorial
def factorial(n):
    if n == 1:          # base case
        return 1
    return n * factorial(n - 1)

print(factorial(5))


# 🔁 Recursion in JavaScript (Comparison)
# Factorial in JS
# function factorial(n) {
#     if (n === 1) {
#         return 1;
#     }
#     return n * factorial(n - 1);
# }

# console.log(factorial(5));


# 📌 Concept is same in Python & JS
# 📌 Syntax slightly different

# | Feature     | Recursion         | Loop         |
# | ----------- | ----------------- | ------------ |
# | Code length | Short             | Longer       |
# | Readability | High (math)       | High (logic) |
# | Memory      | More (call stack) | Less         |
# | Performance | Slower            | Faster       |
# 📌 Use loop if possible
# 📌 Use recursion for tree, divide problems

# 🧠 One-Line Exam Answer
# Recursion is a technique where a function calls itself until a base condition is met.
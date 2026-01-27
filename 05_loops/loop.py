# 🔁 Loops (Python vs JavaScript)
# A loop is used to repeat a block of code multiple times.
# 1️⃣ Types of Loops
# - For Loop: Used to iterate over a sequence (like a list, tuple, or string) a specific number of times.
# - While Loop: Repeats a block of code as long as a specified condition is true.
# | Purpose               | Python            | JavaScript         |
# | --------------------- | ----------------- | ------------------ |
# | Repeat with condition | `while`           | `while`            |
# | Iterate over sequence | `for`             | `for`, `for...of`  |
# | Index-based loop      | `range()`         | classic `for` loop |
# | Loop over key-value   | `for key in dict` | `for...in`         |

# 🟢 WHILE LOOP
# 🔹 Python while
i = 1
while i <= 5:
    print(i)
    i += 1

# 🔹 JavaScript while
# let i = 1;
# while (i <= 5) {
#     console.log(i);
#     i++;
# }
# ✅ Used when number of iterations is unknown.

# 🟢 FOR LOOP (MOST IMPORTANT)
# 2️⃣ FOR LOOP in Python
# Python’s for loop works directly on sequences.
# Example: Loop through numbers
for i in range(1, 6):
    print(i)

# Example: Loop through list
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)

# 3️⃣ FOR LOOP in JavaScript
# 🔹 Classic for loop
# for (let i = 1; i <= 5; i++) {
#     console.log(i);
# }

# 🔹 Loop through array (for...of)
# const fruits = ["apple", "banana", "mango"];

# for (let fruit of fruits) {
#     console.log(fruit);
# }
# 🟡 for...of ≈ Python for

# 🔄 Python range() vs JS Index Loop
# Python
for i in range(0, 5):
    print(i)

# JavaScript
# for (let i = 0; i < 5; i++) {
#     console.log(i);
# }

# 🟢 LOOPING STRINGS
# Python
name = "Sagar"
for ch in name:
    print(ch)

# JavaScript
# let name = "Sagar";
# for (let ch of name) {
#     console.log(ch);
# }

# 🟢 LOOPING LIST vs ARRAY
# Python
nums = [1, 2, 3, 4]
for n in nums:
    print(n)

# JavaScript
# let nums = [1, 2, 3, 4];
# for (let n of nums) {
#     console.log(n);
# }

# 🟢 LOOPING DICTIONARY vs OBJECT
# Python Dictionary
student = {"name": "Sagar", "age": 21}

for key, value in student.items():
    print(key, value)

# JavaScript Object
# const student = { name: "Sagar", age: 21 };

# for (let key in student) {
#     console.log(key, student[key]);
# }

# 🟢 BREAK & CONTINUE
# 🔹 break (stop loop)
# Python
for i in range(1, 6):
    if i == 3:
        break
    print(i)

# JavaScript
# for (let i = 1; i <= 5; i++) {
#     if (i === 3) break;
#     console.log(i);
# }

# 🔹 continue (skip iteration)
# Python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# JavaScript
# for (let i = 1; i <= 5; i++) {
#     if (i === 3) continue;
#     console.log(i);
# }

# 🟢 NESTED LOOPS
# Python
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

# JavaScript
# for (let i = 1; i <= 3; i++) {
#     for (let j = 1; j <= 3; j++) {
#         console.log(i, j);
#     }
# }

# 🟢 ELSE with LOOP (Python ONLY 🔥)
# Python
for i in range(3):
    print(i)
else:
    print("Loop finished")

# ⚠ JavaScript has NO loop else.

# 🟢 Common Mistakes (Exam / Interview)
# | Mistake            | Python              | JavaScript           |
# | ------------------ | ------------------- | -------------------- |
# | Infinite loop      | missing `i += 1`    | missing `i++`        |
# | Wrong comparison   | `=` instead of `==` | `=` instead of `===` |
# | Index out of range | ❌ safer             | ❌ possible           |


# ✅ FINAL SUMMARY
# | Feature         | Python    | JavaScript |
# | --------------- | --------- | ---------- |
# | Simple syntax   | ⭐⭐⭐⭐⭐     | ⭐⭐⭐        |
# | Looping items   | Direct    | `for...of` |
# | Looping objects | `items()` | `for...in` |
# | Loop else       | ✅ Yes     | ❌ No       |

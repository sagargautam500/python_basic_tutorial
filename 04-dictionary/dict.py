# 1️⃣ What is a Dictionary? (Python)
# A dictionary is a collection of key : value pairs.
# Keys must be unique
# Keys are usually string / number / tuple
# Values can be any data type
# Dictionaries are mutable (can be changed)

# Example (Python)
student = {
    "name": "Sagar",
    "age": 21,
    "course": "BSc CSIT",
    "is_student": True
}

# 2️⃣ JavaScript Object (Same concept)
# In JavaScript, the same thing is called an object.

# Example (JavaScript)
# const student = {
#     name: "Sagar",
#     age: 21,
#     course: "BSc CSIT",
#     isStudent: true
# };

# 3️⃣ Dictionary vs Object (Quick Comparison)
# | Feature          | Python Dictionary          | JavaScript Object       |
# | ---------------- | -------------------------- | ----------------------- |
# | Name             | `dict`                     | `object`                |
# | Syntax           | `{ key: value }`           | `{ key: value }`        |
# | Mutable          | ✅ Yes                      | ✅ Yes                   |
# | Access value     | `dict[key]`                | `obj.key` or `obj[key]` |
# | Looping          | `for key in dict`          | `for...in`              |
# | Built-in methods | Many (`keys()`, `items()`) | Fewer (Object methods)  |

# 4️⃣ Accessing Values
# Python
print(student["name"])
print(student.get("age"))

# JavaScript
# console.log(student.name);
# console.log(student["age"]);

# 5️⃣ Adding New Key-Value Pair
# Python
student["email"] = "sagar@gmail.com"

# JavaScript
# student.email = "sagar@gmail.com";

# 6️⃣ Updating Value
# Python
student["age"] = 22

# JavaScript
# student.age = 22;

# 7️⃣ Deleting Data
# Python
# del student["course"]

# JavaScript
# delete student.course;


# 8️⃣ Important Dictionary Methods (Python)
# 🔹 keys()
print(student.keys())

# 🔹 values()
print(student.values())

# 🔹 items()
print(student.items())

# 🔹 get()
print(student.get("name"))
# (⚠ safer than student["name"])

# 🔹 update()
student.update({"age": 23, "city": "Bhaktapur"})

# 9️⃣ Looping Through Dictionary
# Python
for key, value in student.items():
    print(key, ":", value)

# JavaScript
# for (let key in student) {
#     console.log(key + ":", student[key]);
# }


# 🔟 Nested Dictionary / Object
# Python
user = {
    "name": "Sagar",
    "skills": {
        "frontend": "React",
        "backend": "Node.js"
    }
}

# JavaScript
# const user = {
#     name: "Sagar",
#     skills: {
#         frontend: "React",
#         backend: "Node.js"
#     }
# };


# 1️⃣1️⃣ Dictionary with Different Data Types
# Python
data = {
    1: "one",
    "two": 2,
    (3, 4): "tuple key"
}
# ⚠ JavaScript does not support tuple keys like Python.


# 1️⃣2️⃣ When to Use Dictionary / Object?
# ✅ Use when:
# Data has meaningful keys
# You want fast lookup
# You want structured data

# Example:
# User profile
# API response
# Configuration data

# ✅ Final Simple Difference
# 👉 Python Dictionary = JavaScript Object
# 👉 Same purpose, slightly different syntax
# 👉 Python has more built-in methods
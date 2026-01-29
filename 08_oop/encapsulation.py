# 🔐 5️⃣ Encapsulation (Data Protection)
# Binding data + methods together.

# 🔷 Difference: Abstraction vs Encapsulation
# | Feature | Abstraction    | Encapsulation        |
# | ------- | -------------- | -------------------- |
# | Purpose | Hide logic     | Protect data         |
# | Focus   | What to do     | How data is accessed |
# | Example | Abstract class | Private variables    |


# 🔷 What is Encapsulation? (Very Simple)
# Encapsulation = Wrapping data + methods together and controlling access

# 👉 Data is protected
# 👉 Direct access is restricted

# 📌 Real-life example:
# Capsule medicine 💊
# Inside: medicine (data)
# Outside: capsule (protection)

# 🔹 One-line Exam Definition ⭐
# Encapsulation is the process of binding data and methods together and restricting direct access to data.

# 🔷 Why Encapsulation is Needed?
# ✔ Protect data from misuse
# ✔ Improve security
# ✔ Control modification of variables
# ✔ Make code clean & maintainable

# 🔷 Encapsulation in Python
# | Type      | Syntax   | Meaning                      |
# | --------- | -------- | ---------------------------- |
# | Public    | `name`   | Accessible everywhere        |
# | Protected | `_name`  | Use inside class & child     |
# | Private   | `__name` | Accessible only inside class |

# 🟢 Public Variable Example
class Student:
    def __init__(self, name):
        self.name = name

s = Student("Sagar")
print(s.name)
# ✔ Accessible directly

# 🟡 Protected Variable Example
class Student:
    def __init__(self, name):
        self._name = name

s = Student("Sagar")
print(s._name)   # Allowed but not recommended

# 📌 _ = "internal use only" (convention)
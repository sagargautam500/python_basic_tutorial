# 🟢 1️⃣ Class (Blueprint)
# A class is a blueprint or template.

# Python Example
class Student:
    name = "Sagar"
    age = 21

# JavaScript Equivalent
# class Student {
#     constructor() {
#         this.name = "Sagar";
#         this.age = 21;
#     }
# }

# 🟢 2️⃣ Object (Real Entity)
# An object is an instance of a class.

# Python
s1 = Student()
print(s1.name)
print(s1.age)

# JavaScript
# let s1 = new Student();
# console.log(s1.name);

# 🟢 3️⃣ Constructor (__init__)
# Constructor initializes object data.

# Python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Sagar", 21)
print(s1.name)

# JavaScript
# class Student {
#     constructor(name, age) {
#         this.name = name;
#         this.age = age;
#     }
# }
# 📌 self (Python) ≈ this (JS)

# 🟢 4️⃣ Methods (Functions in Class)
# Python
class Student:
    def show(self):
        print("Student name:", self.name)

# JavaScript
# class Student {
#     show() {
#         console.log("Student name:", this.name);
#     }
# }
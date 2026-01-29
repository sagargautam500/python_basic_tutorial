# 1️⃣ What is Polymorphism? (Simple Meaning)
# Polymorphism = One name, many forms
# 👉 Same method/function name, but different behavior depending on:
# object
# data
# situation

# 📌 Real-life example:
# “Speak”
# Human → speaks language
# Dog → barks
# Cat → meows
# Same action, different behavior ✔️

# 2️⃣ Why Polymorphism is Important?
# ✔ Makes code flexible
# ✔ Reduces duplicate code
# ✔ Improves maintainability
# ✔ Core concept in OOP interviews & exams

# 3️⃣ Types of Polymorphism in Python
# Python mainly supports:
# Method Overriding (Runtime Polymorphism)
# Duck Typing
# Operator Overloading

# (There is no traditional method overloading like Java/C++)

# 🔹 1. Method Overriding (Most Important)
# 👉 Same method name, different class behavior
# Python Example
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

a = Animal()
d = Dog()
c = Cat()

a.speak()
d.speak()
c.speak()

# Output
# Animal makes a sound
# Dog barks
# Cat meows
# 📌 Same method speak(), different output → Polymorphism

# 7️⃣ When to Use Polymorphism?

# ✔ When multiple classes share common behavior
# ✔ When you want clean & scalable code
# ✔ Frameworks, APIs, game logic, backend systems
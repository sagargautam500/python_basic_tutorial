# 🔷 What is Abstraction? (Very Simple)
# Abstraction = Hide implementation, show only what is needed

# 👉 You use something
# 👉 You don’t care how it works internally

# 📌 Real-life example:
# You use ATM
# You press buttons
# You don’t know how bank server works inside
# That’s abstraction.

# 🔹 One-line Exam Definition ⭐
# Abstraction is the process of hiding internal details and showing only essential features to the user.

# 🔷 Why Abstraction is Needed?
# ✔ Reduce complexity
# ✔ Increase security
# ✔ Improve code maintainability
# ✔ Force correct structure in large projects

# 🔷 How Abstraction Works in Python?
# Python uses:

# ✅ Abstract Classes
# (from abc module)

# 🔹 What is an Abstract Class?
# A class that cannot be instantiated
# Contains abstract methods
# Child class must implement abstract methods

# 🔹 Abstract Method
# Method without body
# Only method name is defined

# 🔷 Key Rules of Abstraction (Important)
# ✔ Abstract class cannot be instantiated
# ✔ Abstract method must be overridden
# ✔ Abstract class can have normal methods
# ✔ Used mainly in large systems


#real world example::
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

class Bike(Vehicle):
    def start(self):
        print("Bike starts with kick")

class Car(Vehicle):
    def start(self):
        print("Car starts with key")

b = Bike()
c = Car()

b.start()
c.start()

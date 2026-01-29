# 🧠 What is OOP? (Very Simple)
# OOP is a way of programming where we model real-world things using objects and classes.

# 📌 Example:
# Car
# Student
# Bank Account

# Each has:
# Data → variables
# Behavior → functions

# 🔷 Core Concepts of OOP (EXAM VERY IMPORTANT 🔥)

# 1️⃣ Class
# 2️⃣ Object
# 3️⃣ Encapsulation
# 4️⃣ Inheritance
# 5️⃣ Polymorphism
# 6️⃣ Abstraction

# 🧠 Exam One-Line Definitions
# Class: Blueprint of object
# Object: Instance of class
# Encapsulation: Data hiding
# Inheritance: Code reuse
# Polymorphism: One method, many forms
# Abstraction: Hide details

#Bank account example
class Bank:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amt):
        self.balance += amt

    def show(self):
        print(self.balance)

b = Bank(1000)
b.deposit(500)
b.show()

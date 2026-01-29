# 🧬 What is Inheritance? (Very Easy)
# Inheritance allows one class (child) to use properties and methods of another class (parent).

# 📌 Purpose:
# Code reusability
# Easy maintenance
# Logical hierarchy

# 🧠 Real-Life Example
# 👨 Parent → 👦 Child

# Child:
# Gets parent’s features
# Same idea in programming.

# 🔷 Basic Syntax (Python)
class Parent:
    pass

class Child(Parent):
    pass

# 🟢 Example 1: Simple Inheritance
# Parent Class
class Animal:
    def eat(self):
        print("Animal eats")

# Child Class
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Object Creation
d = Dog()
d.eat()     # inherited
d.bark()    # own method
# ✔ Dog can use eat() even though it’s not defined inside it.


# 🟢 Example 2: Constructor in Inheritance
# Parent Class
class Person:
    def __init__(self, name):
        self.name = name

# Child Class
class Student(Person):
    def __init__(self, name, roll):
        self.roll = roll
# ❌ Problem: name is not initialized.

# ✅ Correct Way: Using super()
class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll

# Object
s = Student("Sagar", 101)
print(s.name)
print(s.roll)
# 📌 super() calls parent constructor.


# 🟢 Types of Inheritance (EXAM VERY IMPORTANT 🔥)
# 1️⃣ Single Inheritance
# A → B

class A:
    def showA(self):
        print("Class A")

class B(A):
    def showB(self):
        print("Class B")


# 2️⃣ Multiple Inheritance (Python Supports 🔥)
# A   B
#  \ /
#   C

class Father:
    def work(self):
        print("Father works")

class Mother:
    def care(self):
        print("Mother cares")

class Child(Father, Mother):
    pass

c = Child()
c.work()
c.care()
# 📌 JavaScript ❌ does NOT support this.


# 3️⃣ Multilevel Inheritance
# A → B → C
class Grandfather:
    def house(self):
        print("House")

class Father(Grandfather):
    def car(self):
        print("Car")

class Son(Father):
    def bike(self):
        print("Bike")


# 4️⃣ Hierarchical Inheritance
#      A
#     / \
#    B   C
class Animal:
    def eat(self):
        print("Eat")

class Dog(Animal):
    def bark(self):
        print("Bark")

class Cat(Animal):
    def meow(self):
        print("Meow")


# 5️⃣ Hybrid Inheritance
# Combination of two or more types

# class A:
#     pass

# class B(A):
#     pass

# class C(A):
#     pass

# class D(B, C):
    pass


# 🟡 Python vs JavaScript (Inheritance)
# | Feature              | Python       | JavaScript |
# | -------------------- | ------------ | ---------- |
# | Syntax               | `class B(A)` | `extends`  |
# | Multiple inheritance | ✅ Yes       | ❌ No    |
# | super                | `super()`    | `super()`  |
# | Method override      | Simple       | Simple     |


# 🔷 What is super?
# super is used to access methods or constructors of the parent class from the child class.
# 📌 Mainly used in inheritance

# 🔑 Why Do We Need super?
# Without super:
# Parent class variables may not initialize
# Parent methods may not run

# With super:
# Parent constructor runs
# Parent methods can be reused
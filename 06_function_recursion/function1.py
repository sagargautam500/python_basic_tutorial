# 🔷 Default Parameters
# Python
def greet(name="User"):
    print("Hello", name)

greet()
greet("Sagar")

# JavaScript
# function greet(name = "User") {
#     console.log("Hello", name);
# }

# 🔷 Keyword Arguments (Python ONLY 🔥)
def student(name, age):
    print(name, age)

student(age=21, name="Sagar")
# ❌ JavaScript does NOT support keyword arguments
# (JS uses objects instead)


# 🔷 Variable Scope
# Local Variable
def test():
    x = 10
    print(x)

# Global Variable
x = 5

def test():
    print(x)

# JavaScript (similar concept)
# let x = 5;

# function test() {
#     console.log(x);
# }

# 🔷 *args and **kwargs (Python Special)
# *args → multiple positional arguments
def total(*nums):
    print(nums)

total(1, 2, 3)

# **kwargs → key-value arguments
def info(**data):
    print(data)

info(name="Sagar", age=21)
# 📌 JavaScript equivalent → ...rest and objects

# 🔷 Lambda Function (Arrow Function)
# Python Lambda
add = lambda a, b: a + b
print(add(2, 3))

# JavaScript Arrow Function
# const add = (a, b) => a + b;
# console.log(add(2, 3));


#Function types summary:
# | Type           | Python    | JavaScript |
# | -------------- | --------  | ---------- |
# | Normal         | `def`     | `function` |
# | Return         | `return`  | `return`   |
# | Default args   | ✅        | ✅        |
# | Keyword args   | ✅        | ❌        |
# | Lambda / Arrow | `lambda`   | `=>`      |

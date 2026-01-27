name="sagar"
age=22
price=23.44

print("my name is",name)
print("my age is",age)

print(type(name))

is_student = True
is_admin = False
result = None

# List (list) – like JS Array
numbers = [1, 2, 3, 4]  #list like array
print(numbers[0])  # 1
names = ["Ram", "Shyam", "Sagar"]

# Tuple (tuple) – Immutable list=>Cannot change value.
colors = ("red", "green", "blue")


# Set (set) – Unique values
nums = {1, 2, 3, 3}
print(nums)   # {1, 2, 3}


# Dictionary (dict) – like JS Object
student = {
    "name": "Sagar",
    "age": 22,
    "course": "CSIT"
}
print(student["name"])

# 🔑 Checking Data Type
x = 10
print(type(x))

# Dynamic Typing (Very Important)
x = 10
x = "Hello"
print(x)

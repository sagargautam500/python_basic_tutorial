# 🔷 String in Python
# 1️⃣ What is a String?
# A string is a sequence of characters enclosed in quotes.
name = "Sagar"
city = 'Bhaktapur'

# 2️⃣ Creating Strings
s1 = "Hello"
s2 = 'World'
s3 = """Python Language"""
# ✔ Single quotes
# ✔ Double quotes
# ✔ Triple quotes (multi-line)

# 3️⃣ String Indexing
# Index starts from 0.
text = "Python"
print(text[0])   # P
print(text[3])   # h
# Negative Indexing
print(text[-1])  # n
print(text[-2])  # o

# 4️⃣ String Slicing
text = "Python"
print(text[0:4])   # Pyth
print(text[2:])    # thon
print(text[:3])    # Pyt
print(text[-4:-1]) # tho

# 5️⃣ Strings are Immutable ❗
# You cannot change characters.
text = "Python"
text[0] = "J"   # ❌ Error
# Correct way:
text = "Jython"

# 6️⃣ String Length
text = "Python"
print(len(text))   # 6


# 🔷 Important String Operators
# 1️⃣ Concatenation (+)
a = "Hello"
b = "World"
print(a + " " + b)

# 2️⃣ Repetition (*)
print("Hi " * 3)

# 3️⃣ Membership (in, not in)
text = "Python"
print("Py" in text)      # True
print("Java" not in text) #True

# 🔷 Important String Methods (VERY IMPORTANT).........................
# 1️⃣ lower() / upper()
text = "PyThOn"
print(text.lower())  # python
print(text.upper())  # PYTHON

# 2️⃣ capitalize() / title()
text = "python language"
print(text.capitalize())  # Python language
print(text.title())       # Python Language

# 3️⃣ strip() / lstrip() / rstrip()
# Remove spaces.
text = "  hello  "
print(text.strip())
print(text.lstrip())
print(text.rstrip())

# 4️⃣ replace()
text = "I like Java"
print(text.replace("Java", "Python"))

# 5️⃣ find() / index()
text = "Python"
print(text.find("t"))   # 2
print(text.find("z"))   # -1
print(text.index("t"))  # 2
# text.index("z")  ❌ Error
# 📌 find() is safer

# 6️⃣ count()
text = "banana"
print(text.count("a"))  # 3

# 7️⃣ startswith() / endswith()
text = "python.py"
print(text.startswith("py"))  # True
print(text.endswith(".py"))   # True

# 8️⃣ split()
text = "Python is easy"
words = text.split()
print(words)
# Output:
# ['Python', 'is', 'easy']

# 9️⃣ join()
words = ["Python", "is", "easy"]
text = " ".join(words)
print(text)

# 🔟 isalpha() / isdigit() / isalnum()
print("Python".isalpha())  # True
print("123".isdigit())    # True
print("Py123".isalnum())  # True

# 1️⃣1️⃣ String Formatting (Important)
# Old Style
name = "Sagar"
age = 22
print("My name is", name, "and age is", age)
# format()
print("My name is {} and age is {}".format(name, age))

# f-string (BEST 🔥)
print(f"My name is {name} and age is {age}")

# 🔷 Escape Characters
print("Hello\nWorld")
print("Hello\tWorld")
print("He said \"Hello\"")

# 🔷 Loop Through String
text = "Python"
for ch in text:
    print(ch)

# 🔑 Exam Important Points

# ✔ Strings are immutable
# ✔ Index starts from 0
# ✔ split() → string to list
# ✔ join() → list to string
# ✔ find() returns -1
# ✔ f-strings are fastest
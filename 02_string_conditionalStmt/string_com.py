# 🔷 String: JavaScript vs Python
# 1️⃣ Creating Strings
# JavaScript	Python
# "Hello"	      "Hello"
# 'Hello'	      'Hello'
# `Hello`	      """Hello"""

# let name = "Sagar"; #js
# name = "Sagar"      #python

# 2️⃣ String Length
# JavaScript
# let text = "Python";
# console.log(text.length);

# Python
text = "Python"
print(len(text))

# 3️⃣ String Indexing
# JavaScript
# let text = "Python";
# console.log(text[0]);   // P
# console.log(text[3]);   // h

# Python
text = "Python"
print(text[0])   # P
print(text[3])   # h
# ✔ Same indexing
# ✔ Starts from 0

# 4️⃣ Negative Indexing
# JavaScript
text[text.length - 1];

# Python
text[-1]   # last character
# ✔ Python is easier here

# 5️⃣ String Slicing / Substring
# JavaScript
# text.substring(0, 4);   // Pyth
# text.slice(2);          // thon

# Python

text[0:4]   # Pyth
text[2:]    # thon

# 6️⃣ Strings are Immutable (Both)
# JavaScript
# text[0] = "J";   // ❌ not allowed

# Python
text[0] = "J";   # ❌ error
# ✔ Strings cannot be changed directly

# 7️⃣ String Concatenation
# JavaScript
# "Hello" + " World"

# Python
"Hello" + " World"

# 8️⃣ String Repetition
# JavaScript
# "Hi ".repeat(3);

# Python
"Hi " * 3

# 9️⃣ Case Conversion
# JavaScript	       Python
# toLowerCase()	       lower()
# toUpperCase()	       upper()
# text.toUpperCase(); text.upper()

# 🔟 Remove Spaces
# JavaScript	Python
# trim()	        strip()
# ❌	lstrip(), rstrip()
# text.trim();
# text.strip()

# 1️⃣1️⃣ Replace Text
# JavaScript
# text.replace("Java", "Python");

# Python
text.replace("Java", "Python")

# 1️⃣2️⃣ Find Text
# JavaScript	Python
# indexOf()	    find()
# returns -1	returns -1
# text.indexOf("a");
# text.find("a")

# 1️⃣3️⃣ Split String
# JavaScript
# text.split(" ");

# Python
text.split()

# 1️⃣4️⃣ Join String
# JavaScript
# words.join(" ");

# Python
# " ".join(words)

# 1️⃣5️⃣ Check String Content
# JavaScript	        Python
# Regex / methods 	isalpha()
# 	               isdigit()
# 	               isalnum()
#                    "123".isdigit()   # True

# 1️⃣6️⃣ String Formatting
# JavaScript (Template Literal)
# let name = "Sagar";
# console.log(`My name is ${name}`);

# Python (f-string)
name = "Sagar"
print(f"My name is {name}")


# 🔥 Very similar and powerful
# 🔑 Final Comparison Summary (Exam)

# ✔ Syntax is very similar
# ✔ Python has simpler slicing & negative indexing
# ✔ Methods names differ but purpose same
# ✔ f-strings ≈ template literals
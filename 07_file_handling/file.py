# 📂 What is File Handling?
# File handling means reading data from a file or writing data into a file.

# 📌 Used to:
# Store data permanently
# Read logs, configs, text files
# Work with real applications

# 🧠 Types of File Operations
# 1️⃣ Create a file
# 2️⃣ Write to a file
# 3️⃣ Read from a file
# 4️⃣ Append to a file
# 5️⃣ Close a file

# 🔷 File Handling in Python (BASIC)
# 🔹 Syntax
# file = open("filename", "mode")

# Modes (VERY IMPORTANT)
# | Mode   | Meaning           |
# | ------ | ----------------- |
# | `"r"`  | Read              |
# | `"w"`  | Write (overwrite) |
# | `"a"`  | Append            |
# | `"x"`  | Create            |
# | `"rb"` | Read binary       |
# | `"wb"` | Write binary      |

# 🔷 File Methods (IMPORTANT)
# | Method         | Work           |
# | -------------- | -------------- |
# | `read()`       | Read all       |
# | `readline()`   | Read one line  |
# | `readlines()`  | Read all lines |
# | `write()`      | Write text     |
# | `writelines()` | Write multiple |

# 🟢 1️⃣ Create & Write to a File
# file = open("data.txt", "w")
# file.write("Hello Python File")
# file.close()
# 📌 "w" creates file if not exists
# 📌 Overwrites old data

# 🟢 2️⃣ Read from a File
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()

# 🟢 3️⃣ Append to a File
# file = open("data.txt", "a")
# file.write("\nWelcome Sagar")
# file.close()
# 📌 Adds data at the end
# 📌 Old data stays safe

# 🟢 4️⃣ Read Line by Line
file = open("data.txt", "r")

for line in file:
    print(line)

file.close()

# 🟢 5️⃣ Using with Statement (BEST PRACTICE ⭐)
with open("data.txt", "r") as file:
    print(file.read())
# ✔ Automatically closes file
# ✔ Cleaner and safer

# 🔷 Writing Multiple Lines
lines = ["Hello\n", "Python\n", "File Handling\n"]

with open("data1.txt", "w") as file:
    file.writelines(lines)


# 🔷 Check if File Exists
import os

if os.path.exists("data.txt"):
    print("File exists")



# Deleting a File
# using the os module
# Module (like a code library) is a file written by another programmer that generally hasa functions we can use.
# os.remove("filename")
import os 
os.remove( "data2.txt" ) 

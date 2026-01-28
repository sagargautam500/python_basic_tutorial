# 🔥 Python vs JavaScript (File Handling)
# | Feature     | Python     | JavaScript  |
# | ----------- | ---------- | ----------- |
# | Simplicity  | ⭐⭐⭐⭐⭐      | ⭐⭐⭐         |
# | Built-in    | `open()`   | `fs` module |
# | Auto close  | `with`     | Manual      |
# | Readability | Very clean | Verbose     |

# 🔁 File Handling in JavaScript (Comparison)
# Reading a File (Node.js)
# const fs = require("fs");

# const data = fs.readFileSync("data.txt", "utf8");
# console.log(data);

# Writing a File
# fs.writeFileSync("data.txt", "Hello JS File");

# 🧠 Memory Trick (Exam)
# open → read/write → close
# Use with open() whenever possible

# ✍ Example Program (Exam Style)
# WAP to write name into a file and read it
with open("name.txt", "w") as f:
    f.write("Sagar Gautam")

with open("name.txt", "r") as f:
    print(f.read())

# 🟢 1️⃣ Create & Write to a File
file = open("data3.txt", "w")
file.write("Hello Python File")
file.close()

# 🟢 2️⃣ Read from a File
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()
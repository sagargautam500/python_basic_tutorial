# Let‘s Practice
# Create a new file “practice.txt” using python. Add the following data in it: 
# Hi everyone
# we are learning File I/O
# using Java. I like programming in Java.
with open("practice.txt", "w") as file:
    file.write(
        "Hi everyone\n"
        "we are learning File I/O\n"
        "using Java. I like programming in Java."
    )


# WAF that replace all occurrences of “java” with “python” in above file.
def replace_java_with_python():
    with open("practice.txt", "r") as file:
        data = file.read()

    data = data.replace("Java", "Python")

    with open("practice.txt", "w") as file:
        file.write(data)

replace_java_with_python()

# Search if the word “learning” exists in the file or not. 
with open("practice.txt", "r") as file:
    data = file.read()

if "learning" in data:
    print("The word 'learning' exists in the file")
else:
    print("The word 'learning' does not exist in the file")

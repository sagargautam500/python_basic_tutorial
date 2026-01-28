# 2️⃣ WAF to find the line number where the word “learning” occurs first
# 👉 Print -1 if not found

def find_learning():
    with open("practice.txt", "r") as file:
        lines = file.readlines()

    for i in range(len(lines)):
        if "learning" in lines[i]:
            return i + 1   # line numbers start from 1

    return -1

result = find_learning()
print(result)

# 1️⃣ From a file containing numbers separated by comma, print the count of even numbers
# 📄 Example file: numbers.txt

# with open("numbers.txt","w") as file:
#     file.write("1,2,3,4,5,6,8,10")


with open("numbers.txt", "r") as file:
    data = file.read()

numbers = data.split(",")

count = 0
for num in numbers:
    if int(num) % 2 == 0:
        count += 1

print("Count of even numbers:", count)
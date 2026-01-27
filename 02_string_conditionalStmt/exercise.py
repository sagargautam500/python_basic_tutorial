# Let‘s Practice
# WAP to check if a number entered by the user is odd or even.
num=int(input("enter number "))

if num % 2 == 0:
    print("even")
else:
    print("odd")


# WAP to find the greatest of 3 numbers entered by the user.
# Prompt the user to enter three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Use the max() function to find the greatest of the three numbers
greatest = max(num1, num2, num3)

# Print the result
print(f"The greatest number among {num1}, {num2}, and {num3} is: {greatest}")


# WAP to check if a number is a multiple of 7 or not.

if num % 7 == 0:
    print(f"{num} is multiple of 7")
else:
    print(f"{num} is not Multiple of 7")


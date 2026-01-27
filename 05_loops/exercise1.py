# Let‘s Practice
# Print numbers from 1 to 5. 
# for i in range(1,6) :
#     print(i)

# Print numbers from 10 to 1. 
j=10
while j>=1:
    print(j)
    j-=1

# for i in range(100, 0, -1):
#     print(i)


# Print the multiplication table of a number n.
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)


# Print the elements of the following list using a loop: 
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100] 
nums=[1, 4, 9, 16, 25, 36, 49, 64, 81,100] 

for n in nums:
    print(n)


# Search for a number x in this tuple using loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100] 
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = int(input("Enter number to search: "))

for i in nums:
    if i == x:
        print("Number found")
        break
else:
    print("Number not found")

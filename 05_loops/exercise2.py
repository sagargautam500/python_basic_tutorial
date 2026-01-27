# WAP to find the sum of first n numbers. (using while)
n=5
i=0
sum=0
while i<=n:
    sum+=i
    i+=1

print("sum=",sum)

# WAP to find the factorial of first m numbers. (using for)
n = int(input("Enter a number: "))

fact = 1

for i in range(1, n + 1):
    fact *= i

print("Factorial of", n, "is:", fact)

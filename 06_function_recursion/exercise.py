# Let‘s Practice
# WAF to print the elements of a list in a single line. ( list is the parameter)
def listmarks(nums):
    for i in nums:
        print(i)
    print("length:",len(nums))
listmarks([1,2,3,4])

# WAF to find the factorial of n. (n is the parameter)
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print("factirial value=",factorial(5))

# WAF to print the length of a list. ( list is the parameter)
def list_length(lst):
    count = 0
    for _ in lst:
        count += 1
    print("Length of list:", count)

list_length([10, 20, 30, 40])


# WAF to convert USD to INR. 
def usd_to_inr(usd):
    inr = usd * 83
    return inr

print(usd_to_inr(10))

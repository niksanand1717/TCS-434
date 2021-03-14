"""
Write a user-friendly program to take a input from user and
print the Fibonacci series upto n terms
"""

n = eval(input("Enter the range: "))
result = 0
num1 = 0
num2 = 1

print(num1,"\n"+str(num2))
for i in range(n):
    result = num1 + num2
    num1 = num2
    num2 = result
    print(result)
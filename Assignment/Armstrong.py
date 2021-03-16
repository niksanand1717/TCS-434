"""
Name - Nikhil Anand
Student ID - 19011717
University Roll Number - 1918508
Section - K
Branch - B. Tech. (CSE)
"""

# Title - Print all Armstrong number between two numbers.

# Program

def length(num):
    count = 0
    while num > 0:
        count += 1
        num //= 10
    return count

def sumofdigits(num):
    sum = 0
    pow = length(num)
    while num != 0:
        last = num % 10
        sum = sum + last**pow
        num = num//10
    return sum

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

count = 0

for num in range(num1, num2+1):
    if num == sumofdigits(num):
        print(num)
        count+=1

print("there are ",count," armstrong numbers between", num1, "to", num2)
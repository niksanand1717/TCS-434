"""
Name - Nikhil Anand
Student ID - 19011717
University Roll Number - 1918508
Section - K
Branch - B. Tech. (CSE)
"""

# title - Printing the reverse of number.

# Program

num = eval(input("Enter a number: "))
temp = num
reverse = 0

while num > 0:
    remainder = num % 10
    reverse = reverse*10 + remainder
    num = int(num/10)

print("Reverse of:", temp, "is:", reverse)
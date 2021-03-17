"""
Name - Nikhil Anand
Student ID - 19011717
University Roll Number - 1918508
Section - K
Branch - B. Tech. (CSE)
"""

# Title - Tuple maximum and minimum

# Program

t1 = ((8, 4), (6, 5), (7, 8), (9, 3))
print("Tuple given:", t1)

lst = []

for element in t1:
    lst.append(element[0]*element[1])

lst = max(lst), min(lst)
lst = tuple(lst)
print("Maximum and minimum of given tuple after multiplication :", lst)
# Input n random number in a list and display list with True and False value. If number is even then True otherwise false.

import random

def oddeven(num):
    if num % 2 == 0: print(num, "even")
    else: print(num, "Odd")

num = int(input("Enter number of random numbers required: "))
rnums = list(random.randint(0, 1000) for i in range(num))

list(map(oddeven, rnums))
# map(oddeven, rnums)

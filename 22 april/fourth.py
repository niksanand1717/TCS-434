"""
Write a python program by utilizing any one of the suitable methods to achieve the following property.
                             If number is even print it’s Square
                             If number is odd print it’s cube.
                             If number is prime print 1.5 times of that number.
"""

def condition(num):
    flag = 0
    if num != 1 or num != 0:
        for i in range(1, num//2+1):
            if num%i == 0:
                flag+=1
    if flag == 1:return (num*1.5)
    if num%2 == 0:return (num**2)
    else:return (num**3)


nums = list(map(int, input("Enter numbers separated by space: ").split()))
resnums = list(map(condition, nums))
print(resnums)
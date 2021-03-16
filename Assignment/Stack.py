"""
Name - Nikhil Anand
Student ID - 19011717
University Roll Number - 1918508
Section - K
Branch - B. Tech. (CSE)
"""

# Title - Implementation of stack using list.

# Program

size = int(input("Enter the size of stack: "))
top = -1
list1 = []

def push(list1, top, size):
    if top == size - 1:
        print("Overflow\n\n")
    else:
        top += 1
        list1.append(eval(input("Enter a number: ")))
        print("\n\n")
    return list1, top

def pop(list1, top, size):
    if top == -1:
        print("Underflow\n\n")
    else:
        poped = list1.pop(top)
        top -= 1
        print("Element poped:", poped, "\n\n")
    return list1, top

def peek(list1, top):
    print("Top Most element:", list1[top],"\n\n")

def display(list1):
    print("Stack:", list1,"\n\n")

while True:
    print("Press 1 to push an element\n"+
          "Press 2 to pop an element\n"+
          "Press 3 to peek\n"+
          "Press 4 to display stack\n"+
          "Press 5 to exit the program\n")
    choice = input("Choice: ")

    if choice == '1':
        (list1, top) = push(list1, top, size)
    elif choice == '2':
        (list1, top) = pop(list1, top, size)
    elif choice == '3':
        peek(list1, top)
    elif choice == '4':
        display(list1)
    elif choice == '5':
        break
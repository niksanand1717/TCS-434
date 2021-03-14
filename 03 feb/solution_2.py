num1 = eval(input("Enter the first number: "))
num2 = eval(input("Enter the second number: "))

count1, count2 = 0, 0
print("\n\nNumbers divisible by both 3 and 5")
for num in range(num1, num2+1):
    if num%3 == 0 and num%5 == 0:
        print(num)
        count1+= 1

print("Total numbers of numbers:",count1)


print("\n\nNumbers divisible by 3 or 5")
for num in range(num1, num2+1):
    if num%3 == 0 or num%5 == 0:
        print(num)
        count2+=1

print("Total numbers of numbers:",count2)
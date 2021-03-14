sum, i = 0, 1

nth_number = eval(input("Enter the nth number: "))

while i <= nth_number:
    if i % 2 == 0:
        sum += i ** 2
        i += 1
    else:
        sum += i**3
        i += 1

print("Sum :", sum)
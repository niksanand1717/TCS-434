def factors(num):
    for i in range(1, (num//2)+1):
        if num%i == 0:
            print(i)
    print(num)

num = input("Enter a number to find it's factors: ")
factors(int(num))
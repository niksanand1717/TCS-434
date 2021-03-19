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

all = even = odd = num = 1
all_lst = []
elst = []
olst = []

while (all and even and odd) < 10:
    if num % sumofdigits(num) == 0 and all != 10:
        all_lst.append(num)
        all += 1
    if num % 2 == 0 and even != 10:
        elst.append(num)
        even += 1
    elif odd != 10:
        olst.append(num)
        odd += 1
    num += 1

print("First 10 Harshad Number:", all_lst)
print("First 10 even Harshad Number:", elst)
print("First 10 odd Harshad Number:", olst)
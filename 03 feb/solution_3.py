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

count = 0
for num in range(1, 10000+1):
    if num == sumofdigits(num):
        print(num)
        count+=1
#if __name__ == "__main__":
 #   count = 0
  #  for num in range(1, 10000+1):
   #     if num == sumofdigits(num):
    #        print(num)
     #       count+=1

print("there are ",count," armstrong numbers between 1 to 10000")
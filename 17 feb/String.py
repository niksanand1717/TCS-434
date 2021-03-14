str1 = input("Enter 1st string: ")
str2 = input("Enter 2nd string: ")

if str2 not in str1:
    print(str1+" "+str2)
elif str2 in str1:
    # str1 = str1[0:str1.index(str2)]
    str1 = str1.replace(str2, "\b")
    print(str1)
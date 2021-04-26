# Input n string in a list and print all the strings if and only if started with vowels

strnum = int(input("Enter number of strings you want to enter: "))
strs=[]
for i in range(strnum):
    strs.append(input(f'Enter string {i+1}: '))
print("Strings started with vowels:", list(filter(lambda a: a[0].lower() in 'aeiou', strs)))
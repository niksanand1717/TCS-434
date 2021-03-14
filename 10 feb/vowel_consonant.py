vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

vC, cC = 0, 0

sentence = input("Enter the string: ")

for word in sentence:
    if (word >= 'A' and word <= 'Z') or (word >= 'a' and word <= 'z'):
        if word in vowels:
            vC += 1
        else: cC +=1

print("Vowel: ",vC)
print("Consonant: ",cC)
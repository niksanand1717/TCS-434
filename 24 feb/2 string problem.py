str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

charinstr1, charinstr2 = 0, 0

for chars in str1:
    if chars != ' ':
        charinstr1 += 1

for chars in str2:
    if chars != ' ':
        charinstr2 += 1

countwords = 0

str1lst = str1.split()
str2lst = str2.split()

for words1 in str1lst:
    for words2 in str2lst:
        if words1 == words2:
            countwords += 1

countchars = 0
evaluated = ''

for chars1 in str1:
    if chars1 != ' ':
        for chars2 in str2:
            if chars1 == chars2 and chars1 not in evaluated:
                countchars += 1
                evaluated += chars1

print("\n\nCharacters in str1 :", charinstr1,"\nCharacters in str2 :", charinstr2)
print(countwords,"word is similar in both the strings")
print(countchars,"characters are similar in both the strings")
import re

pattern = '^[aeiou]'

str1 = input("enter string: ")

print("Following are the words in entered string starting with vowel: ", end=' ')
[print(word, end=' ') for word in str1.split(" ") if re.match(pattern, word)]
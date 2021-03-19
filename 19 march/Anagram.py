"""
Write a program to input two strings and check whether the strings are anagrams of each other or not.
Input1:Silent
Output1:listen
Input2: Knee
Output: Keen
"""
def wordCounter(line):
    counts = dict()

    for word in line:  # .lower():
        if word != " ":
            counts[word] = counts.get(word, 0) + 1

    return counts

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if wordCounter(str1) == wordCounter(str2):
    print("Both are Anagrams")
else:
    print(str1+" and "+str2+" are not anagram")
"""
Name - Nikhil Anand
Student ID - 19011717
University Roll Number - 1918508
Section - K
Branch - B. Tech. (CSE)
"""

# Title - Longest palindrome in the given string

# Program

def palindromeCheck(word):
    drow = word[::-1]
    if word == drow:
        return True
    else:
        return False

string = input("Enter a string: ")
strlst = string.split()
num = 0
longest_word = None
for word in strlst:
    if num > len(word):
        bool = palindromeCheck(word)
        if bool is True:
            longest_word = word

print("Longest palindrome is: ", word)
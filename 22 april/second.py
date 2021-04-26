# Input n strings in a list and print all the strings ending with a specific character provided by the user

def seive(string):
    index = (len(string)-1) - len(match)
    if string[index + 1: ] == match:
        return string


strnum = int(input("Enter num of strings: "))
strs = []

for i in range(0, strnum):
    strs.append(input(f"Enter string {i+1}: "))

global match
matchstr: str = input("Enter the matching character at end of string: ")
match = matchstr
output = list(filter(seive, strs))
print(f"Strings ending with {matchstr}:", output)
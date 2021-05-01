"""Print all the words from a string having length of 3"""

import re

pattern = '(...)$'

input_data = input("input string: ")

print("Following are the words which have length 3: ")

for words in input_data.split(" "):
    if re.match(pattern, words): print(words, end=" ")

message1 = "Hello, welcome to programming"
message2 = "python"
message3 = "Hello"
message4 = "Graphic Era Hill University"

print(message3+" "+message2)

"""
string.index('query')
string.find('query')
    .upper()
    .lower()
    .title()
    .capitalize()
    .swapcase()
    .strip()
    .rstrip()
    .lstrip()
    
ord() <--> chr()
    
    .isdigit()
"""

import re

# pattern = '^[.*a.*][.*b.*]'
pattern = '^[.*a]{5}.*bb'

mobile = input("Enter your string: ")
if re.match(pattern, mobile):
    print('Valid String')
else:
    print("Check your data")
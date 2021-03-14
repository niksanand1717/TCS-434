"""
Write a user-friendly python program to check the password is in proper order or not
1. At least one capital letter.
2. At least one small letter.
3. At least one digit.
4. At least one symbol [@#$^&].
5. Length should be at least 8.
"""


password=input("Enter the password: ")
c_har=0
C_har=0
sc=['@', '#', '$', '^', '&']
scc=0
num=0
totalchar=0

"""
for i in range(len(s)):
    if (s[i]>='A' and s[i]<='Z'):
        Char+=1
    if (s[i]>='a' and s[i]<='z' ):
        char+=1
    if s[i]>='0' and s[i]<='9':
        num+=1
    if s[i] in sc:
        scc+=1
"""

for character in password:
    if (character >= 'A' and character <= 'Z'):
        C_har += 1
    if (character >= 'a' and character <= 'z'):
        c_har += 1
    if character >= '0' and character <= '9':
        num += 1
    if character in sc:
        scc += 1
totalchar = num + scc + c_har+ C_har
if(totalchar>=8 and num>=1 and scc>=1 and C_har>=1 and c_har>=1):
    print("Strong Password")
else:
    if C_har == 0: print("Requires atleast one capital letter")
    if c_har == 0: print("Requires atleast one small letter")
    if num == 0: print("Requires atleast one digit")
    if scc == 0: print("Requires atleast one special character")
    if totalchar < 8: print("Requires atleast 8 characters")
"""Create a python file and count number of this, that, is present in that file"""

file = "file.txt"

fh = open(file, 'r')

That = 0
This = 0
Is = 0

for line in fh:
    for word in line.split():
        if word.lower() == 'this': This += 1
        if word.lower() == 'that': That += 1
        if word.lower() == 'is': Is += 1

print("Number of 'this': ", This)
print("Number of 'that': ", That)
print("Number of 'is': ", Is)
"""Python Program to print the last line from the file"""

filename = "file.txt"

fh = open(filename, mode='r')

file_list = []

for line in fh:
    file_list.append(line)

print(file_list[-1])
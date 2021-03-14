import time
import subprocess as sp

while True:
    line = input("Enter a string: ")
    new_str = ""
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    if len(line) < 10:
        print("enter a valid string")
        time.sleep(2)
        sp.call("clear", shell=True)
        continue
    for i in range(len(line)):
        if line[i] in vowels:
            # line[i] = str(line[i].upper())
            new_str += line[i].swapcase()
        else:
            new_str += line[i]

    print(new_str)
    break
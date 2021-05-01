"""Read this string
        T#H#E# #W#O#R#L#D# #I#S# #R#O#U#N#D#
        and print only the character"""

file = "third_question_file.txt"

def sieve(file):
    result = ""
    fh = open(file, 'r')
    for line in fh:
        for letter in line:
            if ord(letter.upper()) >= 65 and ord(letter.upper()) <= 97 or letter == ' ':
                result += letter
    return result

fh = open(file, 'r')
print("Raw Text in file: ", fh.read())
print("Resultant Text after filtering: ", sieve(file))

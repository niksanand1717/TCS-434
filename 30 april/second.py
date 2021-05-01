"""Count total number of lines, words, character in a file"""

file = "file.txt"

def lines(file):
    fh = open(file, 'r')
    line_count = 0
    for line in fh:
        line_count += 1
    return line_count

def words(file):
    fh = open(file, 'r')
    word_counts = 0
    for line in fh:
        # print(line.split())
        word_counts += len(line.split(" "))
    return word_counts

def characters(file):
    fh = open(file, 'r')
    char_count = 0
    for line in fh:
        for word in line.split():
            char_count += len(word)
    return char_count

print("Lines : ", lines(file))
print("Words : ", words(file))


print("Characters : ", characters(file))
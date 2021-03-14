counts = dict()

line = input("Enter a string: ")

# print("Line Entered: ", line)

for word in line:#.lower():
    counts[word] = counts.get(word, 0) + 1

print('Counts', counts)
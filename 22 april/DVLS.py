def condition(string):
    count = {}
    ideal = { 'a': 2,
              'e': 2,
              'i': 2,
              'o': 2,
              'u': 2}
    for word in string: count[word] = count.get(word, 0) + 1
    print("Lovely String") if count == ideal else print("Ugly String")

volwels = 'aeiou'
string1 = input("Enter a string: ")
string = ""
for word in string1:
    if word != " ": string += word.lower()
condition(string)
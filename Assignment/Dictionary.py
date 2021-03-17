"""
Name - Nikhil Anand
Student ID - 19011717
University Roll Number - 1918508
Section - K
Branch - B. Tech. (CSE)
"""

# Title - Implementation of stack using list.

# Program


name = ["Nikhil Anand", "Ivan Roy", "Pankaj Bhandari", "Ansh Riyal"]
roll_no = [36, 29, 38, 10]
print("Given list of names: ", name, "\n\n")
print("Given list of roll numbers", roll_no, "\n\n")
print("using above two list we can make a dictionary")
dictionary = dict(zip(roll_no, name))
print(dictionary)
print("Keys of dictionary: ", dictionary.keys(), "\n")
print("Values of dictionary: ", dictionary.values(), "\n")
print("Getting key-value pairs of dictionary in list of tuples and sorting them:-")
tp = dictionary.items()
print(sorted(tp))
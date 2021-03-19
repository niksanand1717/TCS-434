"""
Create a dictionary to achieve the following task:
1.Create a dictionary in which consider key as a name of the student and value marks in five subjects.
2.Calculate the sum of the marks of each student and create anew dictionary (Results) having a key as a name of the student and value as total marks.
3.You noticed that you entered wrong marks for subject number 4 update the marks in the original dictionary and re calculate the same.
•Result dictionary will update automatically based on the input change in first dictionary.
"""

def avg(lst):
    avg_lst = []
    for lsti in lst:
        avg_lst.append(sum(lsti)/5)
    return avg_lst

students = ["Nikhil Anand", "Ivan Roy", "Ansh Riyal", "Pankaj Bhandari", "Ajay Negi"]
marks = [[50, 55, 35, 48, 69], [90, 69, 78, 86, 75], [56, 78, 89, 56, 78], [75, 69, 78, 9, 45], [48, 89, 56, 45, 78]]
result = dict(zip(students, marks))
print("Name of students and thier marks in five subjects:", result)

marks_avg = avg(marks)
result_avg = dict(zip(students, marks_avg))
print("Name of students and thier average marks of five subjects:", result_avg, "\n\n")

print("Now changing marks of subject 4 in main dictionary: ")
for key in result.keys():
    result[key][3] = input("Enter the correct marks for subject 4 of "+key+" : ")

marks_avg = avg(marks)
result_avg = dict(zip(students, marks_avg))
print("\n\nName of students and thier average marks of five subjects after correction:", result_avg)
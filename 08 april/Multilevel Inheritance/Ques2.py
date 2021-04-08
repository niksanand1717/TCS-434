class Student():
    name = str()
    studentID = str()
    universityRN = str()

    def getData(self, student_name, student_ID, university_roll_no):
        self.name = student_name
        self.studentID = student_ID
        self.universityRN = university_roll_no

class Grade(Student):
    marks = []
    def getMarks(self):
        print("Enter the marks of 5 subjects: ")
        for i in range(5):
            self.marks.append(float(input()))


class FinalResult(Grade):
    average = 0.0

    def avg(self, marks):
        return sum(self.marks) / len(self.marks)

    def findAverage(self):
        self.average = self.avg(self.marks)

    def ResultDisplay(self):
        string = "\n\nName: "+self.name+"\nStudent ID: "+self.studentID+"\nUniversity Roll Number: "+self.universityRN+"\nTotal Marks: "+str(sum(self.marks))+"\nAverage: "+str(self.average)
        print(string)


student1 = FinalResult()
student1.getData(student_name="Nikhil Anand", student_ID="19011717", university_roll_no="1918508")
student1.getMarks()
student1.findAverage()
student1.ResultDisplay()
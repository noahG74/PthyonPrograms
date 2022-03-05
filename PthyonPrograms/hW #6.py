"""
Author: Noah Gonzales
Date: 3/4/2022
"""
import re
import random

# Question 1
class Student:
    def __init__(self, firstName, lastName, email, allCourse):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.allCourse = allCourse


if __name__ == '__main__':
    namesFile = open('student.txt','r')
    emailFile = open('student.txt','r')
    gradesFile = open('student.txt','r')
    next(namesFile)
    next(emailFile)
    next(gradesFile)
    try:
        names = re.findall('[A-Za-z]+\s',namesFile.read())
        email = re.findall('\w+@islander.tamucc.edu',emailFile.read())
        grades = re.findall('\d{2,3}',gradesFile.read())
    except:
        "File does not exist"
    course = [[grades[0],grades[1],grades[2],grades[3],grades[4],grades[5]],[grades[6],grades[7],grades[8],grades[9],grades[10],grades[11]],[grades[12],grades[13],
             grades[14],grades[15],grades[16],grades[17]],[grades[18],grades[19],grades[20],grades[21],grades[22],grades[23]],[grades[24],grades[25],grades[26],
             grades[27],grades[28],grades[29]],[grades[30],grades[31],grades[32],grades[33],grades[34],grades[35]],[grades[36],grades[37],grades[38],grades[39],
             grades[40],grades[41]],[grades[42],grades[43],grades[44],grades[45],grades[46],grades[47]],[grades[48],grades[49],grades[50],grades[51],grades[52],
             grades[53]],[grades[54],grades[55],grades[56],grades[57],grades[58],grades[59]]]

    student1 = [names[0], names[1],email[0], course[0]]
    student2 = [names[3], names[4],email[1], course[1]]
    student3 = [names[6], names[7],email[2], course[2]]
    student4 = [names[9], names[10],email[3], course[3]]
    student5 = [names[12], names[13],email[4], course[4]]
    student6 = [names[15], names[16],email[5], course[5]]
    student7 = [names[18], names[19],email[6], course[6]]
    student8 = [names[21], names[22],email[7], course[7]]
    student9 = [names[24], names[25],email[8], course[8]]
    student10 = [names[27], names[28],email[9], course[9]]

    newFile = open('student.txt','a')

    students=["Jasmine", "Lara", "Rick", "Devon", "Walter",
              "Thomas", "Chris", "Noah", "Suko", "Karissa",
              "Patrick", "AJ", "Eva", "Logan", "Brandon",
              "Cameron", "Joe", "Jose", "James", "Noel",
              "Nick", "Cutter", "Barbara", "Franky", "Alyssa"]

    course1 = [random.randint(0,100) for i in range(0,25)]
    course2 = [random.randint(0,100) for i in range(0,25)]
    course3 = [random.randint(0,100) for i in range(0,25)]
    course4 = [random.randint(0,100) for i in range(0,25)]
    course5 = [random.randint(0,100) for i in range(0,25)]
    course6 = [random.randint(0,100) for i in range(0,25)]



    for i in range (0,25):
        newFile.write(students[i])
        newFile.write(' ')
        newFile.write(str(course1[i]))
        newFile.write(' ')
        newFile.write(str(course2[i]))
        newFile.write(' ')
        newFile.write(str(course3[i]))
        newFile.write(' ')
        newFile.write(str(course4[i]))
        newFile.write(' ')
        newFile.write(str(course5[i]))
        newFile.write(' ')
        newFile.write(str(course6[i]))
        newFile.write("\n")

    namesFile.close()
    emailFile.close()
    gradesFile.close()
    newFile.close()

# Question 2
def writeFile(f1,f2,f3,final):
    final.write(f1)
    final.write("\n")
    final.write(f2)
    final.write("\n")
    final.write(f3)

def readFile(f1,f2,f3):
    first = f1.read()
    second = f2.read()
    third = f3.read()
    final = open('final.txt','w')
    writeFile(first, second, third,final)
    final.close()

def main():
    try:
        f1 = open('f1.txt','r')
        f2 = open('f2.txt','r')
        f3 = open('f3.txt','r')

        readFile(f1,f2,f3)

        f1.close()
        f2.close()
        f3.close()
    except FileNotFoundError:
        print("Some files are not existent")

main()

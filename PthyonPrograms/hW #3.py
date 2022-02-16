"""
Author: Noah Gonzales
Date: 2/10/2022
"""

#Question 1

class Car():
    def __init__(self, yearModel, make, speed):
        self.yearModel = yearModel
        self.make = make
        self.speed = speed

    def accelerate(self):
        self.speed += 5

    def carbreak(self):
        self.speed -= 5

    def get_Speed (self):
        return self.speed


if __name__ == '__main__':
    car = Car(2021, "Chevy Colorado", 0)
    for temp in range(0,5):
        car.accelerate()
        print ( "The car's speed is", car.get_Speed())
    for temp in range(0,5):
        car.carbreak()
        print ( "The car's speed is", car.get_Speed())
    print(" ")

#Question 2/3

class Employee():
    def __init__(self, name, idNumber, department, jobTitle, fullName, email):
        self.name = name
        self.idNumber = idNumber
        self.department = department
        self.jobTitle = jobTitle
        self.fullName = fullName
        self.email = email

    def titles (self):
        print(self.name," ",self.idNumber," ",self.department," ", self.jobTitle)

    def newTitles (self):
        print(self.fullName," ",self.email)


if __name__ == '__main__':
    print("Name","        "," ID Number"," Department","    ","Job Title")

    employee1 = Employee("Susan Meyers","47899", "   Accounting", "   Vice President","SusanMeyers","susan.meyers@company.com")
    employee1.titles()

    employee2 = Employee("Mark Jones","  39119", "   IT", "           Programmer","MarkJones","  mark.jones@company.com")
    employee2.titles()

    employee3 = Employee("Joy Rogers","  81774", "   Manufacturing", "Engineer","JoyRogers", "  joy.rogers@company.com")
    employee3.titles()
    print(" ")

    print("Full Name", "    Email")
    employee1.newTitles()
    employee2.newTitles()
    employee3.newTitles()

#Question 4

class Course():
    def __init__(self, student, course1, course2, course3, course4, course5, course6):
        self.student = student
        self.course1 = course1
        self.course2 = course2
        self.course3 = course3
        self.course4 = course4
        self.course5 = course5
        self.course6 = course6

    def percentage (self):
        num = self.course1 + self.course2 + self.course3 + self.course4 + self.course5 + self.course6
        percent = num/600
        return (round(percent,2))

def average(course):
    val = 0
    for x in range(0,25):
        val += course[x]
    val /= 25
    return round(val, 2)


if __name__ == '__main__':
    import random

    students=["Jasmine", "Lara", "Rick", "Devon", "Walter",
              "Thomas", "Chris", "Noah", "Suko", "Karissa",
              "Patrick", "AJ", "Eva", "Logan", "Brandon",
              "Cameron", "Joe", "Jose", "James", "Noel",
              "Nick", "Cutter", "Barbara", "Franky", "Alyssa"]

    course1 = [random.uniform(0,100) for i in range(0,25)]
    course2 = [random.uniform(0,100) for i in range(0,25)]
    course3 = [random.uniform(0,100) for i in range(0,25)]
    course4 = [random.uniform(0,100) for i in range(0,25)]
    course5 = [random.uniform(0,100) for i in range(0,25)]
    course6 = [random.uniform(0,100) for i in range(0,25)]

    kid = [Course(students[x],course1[x],course2[x],course3[x],course4[x],course5[x],course6[x]) for x in range (0,25)]

    percents = [kid[x].percentage() for x in range(0,25)]

    size = len(percents)
    for j in range(size):
        for i in range(j+1,size):
            if (percents[j] > percents[i]):
                temp = percents[j]
                percents[j] = percents[i]
                percents[i] = temp
                temp2 = students[j]
                students[j] = students[i]
                students[i] = temp2

    averages = [average(course1),average(course2),average(course3),average(course4),average(course5),average(course6)]

    highest = 0
    for i in range(0,6):
        if averages[highest] < averages[i]:
            highest = i


    print("Student with the highest percentage:", students[24])
    print("Their percentage:", percents[24])
    print("Course with the highest average: Course", highest + 1)
    print("The average was:", averages[highest])

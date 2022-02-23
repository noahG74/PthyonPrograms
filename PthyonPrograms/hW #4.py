"""
Name: Noah Gonzales
Date: 2/21/2022
"""

# Question 1
Employee = {
"47899": {'Name': 'Susan Meyers', 'Department': 'Accounting', 'Job Title': 'Vice President'},
"39119": {"Name": "Mark Jones", "Department": "IT", "Job Title": "Programmer"},
"81774": {"Name": "Joy Rogers", "Department": "Manufacturing", "Job Title": "Engineer"},
}
choice = int(input('1: To look up employee\n'
                   '2: To add a new employee\n'
                   '3: To change an existing employee name, department and job title\n'
                   '4: Delete an employee from the dictionary\n'
                   '5: Quit the program\n'
                   'Please enter a number: '))
if choice == 1:
    num = input('Please enter their ID number: ')
    if num == '47899':
        print("Name:", Employee["47899"]['Name'])
        print("Department:", Employee["47899"]['Department'])
        print("Job Title:", Employee["47899"]['Job Title'])
    elif num == '39119':
        print("Name:", Employee["39119"]['Name'])
        print("Department:", Employee["39119"]['Department'])
        print("Job Title:", Employee["39119"]['Job Title'])
    elif num == '81774':
        print("Name:", Employee["81774"]['Name'])
        print("Department:", Employee["81774"]['Department'])
        print("Job Title:", Employee["81774"]['Job Title'])
elif choice == 2:
    idNumber = input('Enter their ID number: ')
    name = input('Enter their name: ')
    deparment = input('Enter their department: ')
    jobTitle = input('Enter their job title: ')
    Employee[idNumber] = {"Name": name, "Department": deparment, "Job Title": jobTitle}
    print("")
    print("Name:", Employee[idNumber]['Name'])
    print("Department:", Employee[idNumber]['Department'])
    print("Job Title:", Employee[idNumber]['Job Title'])
elif choice == 3:
    val = input('Please enter the ID number of the employee you wish to alter: ')
    newName = input('Enter the new name: ')
    newDeparment = input('Enter their new deparment: ')
    newJobTitle = input('Enter their new job title: ')
    Employee[val] = {"Name": newName, "Department": newDeparment, "Job Title": newJobTitle}
    print("")
    print("The employee's new information is: ")
    print("Name:", Employee[val]['Name'])
    print("Department:", Employee[val]['Department'])
    print("Job Title:", Employee[val]['Job Title'])
elif choice == 4:
    val = input("Please enter the employee's ID you wish you delete: ")
    del Employee[val]
    print("Empolyee is no longer available")
elif choice == 5:
    print("Bye Bye")
    quit()

# Question 2
numbers = []

numbers = [int(input('Please enter a number: ')) for i in range(0,20)]
lowest = numbers[0]
highest = numbers[0]
total = 0
average = 0

for i in range(0,20):
    if (numbers[i] < lowest):
        lowest = numbers[i]
    if(numbers[i] > highest):
        highest = numbers[i]
    total += numbers[i]
average = total/20

print("The lowest number is:",lowest)
print("The highest number is:",highest)
print("The total of all the numbers is :",total)
print("The average of all the numbers is:",average)

# Question 3
squares = {

}
x = int(input("Please enter a number: "))
for i in range(0,x):
    squares[x] = x*x

#Question 4
from random import randint
randomList = [randint(0,100) for i in range(0,20)]
size = len(randomList)
highest = randomList[0]
secondHighest = randomList[0]
count = 0
for i in range(0,20):
    if(randomList[i] > highest):
        secondHighest = highest
        highest = randomList[i]
    if(randomList[i] > secondHighest and randomList[i] < highest):
        secondHighest = randomList[i]
print("Second highest in the list is:",secondHighest)

for j in range(0,size):
    for i in range(0,size):
        if(randomList[j] == randomList[i]):
            count += 1
    if (count == 1):
        randomList.remove(randomList[i])
    size -= count
print(randomList)

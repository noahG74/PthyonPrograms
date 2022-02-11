#C:\Users\noahs\OneDrive\Documents
"""
Name: Noah Gonzales
Question: 1
Date: 1/31/2022
"""
print("Question 1:")
print("My name is Noah Gonzales. I grew up in Poteet, TX. The zip code is 78065.")
print("My number is 210-749-7317, and I am a computer science major.")
print(" ")
"""
Name: Noah Gonzales
Question: 2
Date: 1/31/2022
"""
print("Question 2:")
acres = int(input("Please enter the total number of square feet: "))
print("The number of acres in this tract of land is: ")
print(round(acres/43560,2))
print(" ")

"""
Name: Noah Gonzales
Question: 3
Date: 1/31/2022
"""
print("Question 3:")
print("A car traveling at 70 MPH will go", end = " ")
print(70*6, end =" ")
print("miles in 6 hours")
print("A car traveling at 70 MPH will go", end = " ")
print(70*10, end =" ")
print("miles in 10 hours")
print("A car traveling at 70 MPH will go", end = " ")
print(70*15, end =" ")
print("miles in 15 hours")
print (" ")

"""
Name: Noah Gonzales
Question: 4
Date: 1/31/2022
"""
print("Question 4:")
age = int(input("Please enter your age: "))
if age <= 1:
    print("You are an infant")
elif age < 13 and age > 1:
    print ("You are a child")
elif age < 20 and age >= 13:
    print ("You are a teenager")
else:
    print ("You are an adult")
print (" ")

"""
Name: Noah Gonzales
Question: 5
Date: 1/31/2022
"""
print("Question 5:")
total = 0.00
print("Enter a coin value and try to make it add up to dollar(.01,.05,.10,.25,.50): ")
holder = float(input("Please enter a coin amount(enter 0 to end): "))
while holder != 0:
    total = total + holder
    holder = float(input("Please enter a coin amount(enter 0 to end): "))
if total == 1.00:
    print("Congratulations!! You added them up to a dollar")
elif total < 1.00:
    print ("Oops :/ You unfortunately added to less than a dollar")
    print ("The amount you entered was ",round(total,2))
else:
    print ("Oooo, You went over a dollar")
    print ("The amount you entered was ",round(total,2))
print (" ")

"""
Name: Noah Gonzales
Question: 6
Date: 02/01/2022
"""
print("Question 6:")
yearNumber = int(input("Please enter the year: "))
if yearNumber%100 == 0 and yearNumber%400 == 0:
    print("The number of days in February during the year",yearNumber,"is 29") 
elif yearNumber%100 != 0and yearNumber%4 == 0:
    print("The number of days in February during the year",yearNumber,"is 29")
else:
    print("The number of days in February during the year",yearNumber,"is 28")
print(" ")

"""
Name: Noah Gonzales
Question: 7
Date: 02/01/2022
"""
print("Question 7:")
personsWeight = float(input("Please enter your weight(pounds): "))
personsHeight = float(input("Please enter your height (inches): "))
bodyMassIndex = (personsWeight*703)/(personsHeight*personsHeight)
if bodyMassIndex <= 25 and bodyMassIndex >= 18.5:
    print("You're BMI is",round(bodyMassIndex,2),"which means you have optimal weight")
elif bodyMassIndex < 18.5:
    print("You're BMI is",round(bodyMassIndex,2),"which means you have under weight")
else:
    print("You're BMI is",round(bodyMassIndex,2),"which means you have over weight")
print("")


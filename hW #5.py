"""
Author: Noah Gonzales
Date: 3/1/2022
"""
# Question 1
userString = input("Please enter a string: ")
print("This is what you entered in morse code:")

for i in userString:
    if i == "A" or i == "a":
        print(".-", end = " ")
    if i == "B" or i == "b":
        print("-...", end = " ")
    if i == "C" or i == "c":
        print("-.-.", end = " ")
    if i == "D" or i == "d":
        print("-..", end = " ")
    if i == "E" or i == "e":
        print(".", end = " ")
    if i == "F" or i == "f":
        print("..-.", end = " ")
    if i == "G" or i == "g":
        print("--.", end = " ")
    if i == "H" or i == "h":
        print("....", end = " ")
    if i == "I" or i == "i":
        print("..", end = " ")
    if i == "J" or i == "j":
        print(".---", end = " ")
    if i == "K" or i == "k":
        print("-.-", end = " ")
    if i == "L" or i == "l":
        print(".-..", end = " ")
    if i == "M" or i == "m":
        print("--", end = " ")
    if i == "N" or i == "n":
        print("-.", end = " ")
    if i == "O" or i == "o":
        print("---", end = " ")
    if i == "P" or i == "p":
        print(".--.", end = " ")
    if i == "Q" or i == "q":
        print("--.-", end = " ")
    if i == "R" or i == "r":
        print(".-.", end = " ")
    if i == "S" or i == "s":
        print("...", end = " ")
    if i == "T" or i == "t":
        print("-", end = " ")
    if i == "U" or i == "u":
        print("..-", end = " ")
    if i == "V" or i == "v":
        print("...-", end = " ")
    if i == "W" or i == "w":
        print(".--", end = " ")
    if i == "X" or i == "x":
        print("-..-", end = " ")
    if i == "Y" or i == "y":
        print("-.-", end = " ")
    if i == "Z" or i == "z":
        print("--..", end = " ")
    if i == "0":
        print("-----", end = " ")
    if i == "1":
        print(".-----", end = " ")
    if i == "2":
        print("..---", end = " ")
    if i == "3":
        print("...--", end = " ")
    if i == "4":
        print("....-", end = " ")
    if i == "5":
        print(".....", end = " ")
    if i == "6":
        print("-....", end = " ")
    if i == "7":
        print("--...", end = " ")
    if i == "8":
        print("---..", end = " ")
    if i == "9":
        print("----.", end = " ")
    if i == " ":
        print(" ", end = " ")
    if i == ",":
        print("--..--", end = " ")
    if i == ".":
        print(".-.-.-", end = " ")
    if i == "?":
        print("..--..", end = " ")

# Question 2
def vowelCount(word):
    word = word.lower()
    count = 0
    for i in word:
        if (i == "a" or i == "e" or i == "i" or i == "u" or i =="y"):
            count += 1
    return(count)

def consonantCount(word):
    word = word.lower()
    count = 0
    for i in word:
        if (i != "a" and i != "e" and i != "i" and i != "u" and i !="y"):
            count += 1
    return(count)

word = input("Please enter a word: ")
print("The number of vowels in your word is: ", vowelCount(word))
print("The number of consonants in your word is: ", consonantCount(word))

# Question 3
str1 = "P@#yn@^at^&i5ve"
count = 0
for i in str1:
    count += 1
print("The number of letters, digits, and symbols in",str1, "is:", count)

str1 = "/*Jon is @developer & musician"
newStr = str1[:0] + str1[2:]
newStr1 = newStr[:7] + newStr[8:]
newStr2 = newStr1[:17] + newStr1[18:]
print("")
print("Before:", str1)
print("After:",newStr2)

str1 = "Emma-is-a-data-scientist"
str2 = str1[0:4] + " " + str1[5:7] + " " + str1[8:9] + " " + str1[10:14] + " " + str1[15:24]
print("")
print(str2)

lst = ["a", "e","i","o","u","y", " "]
str1 = "Hello, have a good day"
str1 = str1.lower()
for i in str1:
    if i not in lst:
        str1 = str1[:str1.index(i)]+str1[str1.index(i)+1:]
print("")
print(str1)

# Question 4
import math
i = 0
nums = []
total = 0
count = 1
while count < 100:
    i = int(input("Please enter at least 10 numbers between 0 and 100 or enter a number out of range to stop: "))
    if i < 0 or i > 100:
        if count < 10:
            i = int(input("You need to enter at least 10 numbers: "))
            while i < 0 or i > 100:
                i = int(input("The numbers need to be between 0 and 100: "))
        elif count > 10:
            break
    count += 1
    nums.append(i)

for i in range(0,len(nums)):
    total = nums[i] + total
avg = total/len(nums)

median = int((len(nums) + 1)/2)

deviation = []
for i in range(0,len(nums)):
    total = 0
    total = nums[i] - avg
    deviation.append(round(total*total,2))
total = 0
for i in range(0,len(deviation)):
    total += deviation[i]
variance = total/len(nums)
stanDeviation = math.sqrt(variance)


division = []
total = 0
for i in range(0,len(nums)):
    if i == len(nums):
        break
    elif i != len(nums):
        try:
            division.append(round(nums[i]/(nums[i+1],2)))
        except:
            print("ignored")
            break

print("The average of the numbers in the list:", round(avg,2))
print("The median of the list is:", median)
print("The standard deviation of the numbers:", round(stanDeviation,2))
print(division)

# Question 5
str = "this is the string for the class"
newStr = ""
upperCase = str[0].upper()
upperCase2 = str[5].upper()
upperCase3 = str[8].upper()
upperCase4 = str[12].upper()
upperCase5 = str[19].upper()
upperCase6 = str[23].upper()
upperCase7 = str[27].upper()

for i in range(0,len(str)):
    if i == 0 or i == 5 or i == 8 or i == 12 or i == 19 or i == 23 or i == 27:
        newStr += str[i].upper()
    else:
        newStr += str[i]

print(newStr)
print("")
newStr = ""

for i in range(0,len(str)):
    if i == 0 or i == 5 or i == 8 or i == 12 or i == 19 or i == 23 or i == 27:
        newStr += str[i].upper()
    elif i == 4 or i == 7 or i == 11 or i == 18 or i == 22 or i == 26:
        continue
    else:
        newStr += str[i]

print(newStr)
print("")
newStr = ""

for i in range(0,len(str)):
    if i == 0 or i == 5 or i == 27:
        newStr += str[i].upper()
    elif i == 3 or i == 6 or i == 12 or i == 30 or i == 31:
        newStr += '$'
    elif i == 8 or i == 9 or i == 10 or i == 11:
        continue
    else:
        newStr += str[i]

print(newStr)
print("")
newStr = ""

for i in range(0,len(str)):
    if i == 0 or i == 12 or i == 27:
        newStr += str[i].upper()
    else:
        newStr += str[i]

print(newStr)

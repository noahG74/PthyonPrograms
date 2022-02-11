"""
Name: Noah Gonzales
Date: 2/7/2022
"""
#Question #1(i)
for temp in range(0,5):
    print("")
    for temp2 in range(temp+1):
        print("* ", end="")
print(" ")


#Question #1 (ii)
spaces = 8
for temp in range(0,5):
    print("")
    for temp2 in range(spaces):
        print(end=" ")
    spaces = spaces - 2
    for temp3 in range(temp+1):
        print("* ", end="")
print("")
print(" ")


#Question #2 (i)
num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter another number(bigger than the first one): "))
num3 = num1-num2
num1Fact = 1.0
num2Fact = 1.0
num3Fact = 1.0

#Question #2 (ii)
for temp in range (1,num1 + 1):
    num1Fact = num1Fact* temp
for temp in range (1,num2 + 1):
    num2Fact = num2Fact* temp
for temp in range (1,num3 + 1):
    num3Fact = num3Fact* temp
print(num1Fact/(num2Fact*(num3Fact)))

#Question #2 (iii)
print(num1Fact/num3Fact)
print(" ")
"""
Question #3
Date: 2/7/2022
"""
a = [20,68,41,88,16,40,65,97,85]
size = len(a)
for j in range(size):
    for i in range(j+1, size):
        if(a[j] > a[i]):
           temp = a[j]
           a[j] = a[i]
           a[i] = temp
print(a)
print(" ")

#Question #4
b = [20,68,41,88,16,40,65,97,85]
evenLst = []
oddLst = []
val = 0
val2 = 0
val3 = 0
for temp in b:
    val = val + temp
print(val)
for temp in b:
    if(temp % 2 == 0):
       evenLst.append(temp)
    elif(temp % 2 == 1):
        oddLst.append(temp)
for temp in evenLst:
    val2 = val2 + temp
print(val2)
for temp in oddLst:
    val3 = val3 + temp
print(val3)
print(" ")

#Question #5
low = 2
high = 51
for val in range(low, high):
        for i in range(2,val):
            if val% i == 0:
                break
        else:
            print(val, end=" ")
print(" ")
print(" ")

#Question #6(i)
def triangle():
    for temp in range(0,5):
        print("")
        for temp2 in range(temp+1):
            print("* ", end="")
    print(" ")

def invertedTriangle():
    spaces = 8
    for temp in range(0,5):
        print("")
        for temp2 in range(spaces):
            print(end=" ")
        spaces = spaces - 2
        for temp3 in range(temp+1):
            print("* ", end="")
    print("")
    print(" ")

triangle()
invertedTriangle()

#Question #6(ii)
def mathFunction (n, r):
    num3 = n - r
    nFact = 1
    rFact = 1
    num3Fact = 1
    
    for temp in range (1,n + 1):
        nFact = nFact* temp
    for temp in range (1,r + 1):
        rFact = rFact* temp
    for temp in range (1,num3 + 1):
        num3Fact = num3Fact* temp
        
    print(nFact/(rFact*(num3Fact)))
    print(nFact/num3Fact)
    print(" ")

num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter another number(bigger than the first one): "))
mathFunction (num1, num2)

#question 6(iii)
def sortingFunction(lst):
    size = len(lst)
    for j in range(size):
         for i in range(j+1, size):
            if(lst[j] > lst[i]):
               temp = lst[j]
               lst[j] = lst[i]
               lst[i] = temp
    print(lst)
a = [20,68,41,88,16,40,65,97,85]
sortingFunction(a)
print(" ")

#question 9
loopCounter = 1
while loopCounter <= 10:
    if (loopCounter %2) == 0:
        print(loopCounter, end=" ")
    loopCounter += 1

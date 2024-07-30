#Given 3 distinct numbers a, b, c, you want to find the largest of the 3 by comparing each two at a time. 
#Using elifs (each containing one relational operator) write a program that reads 3 distinct numbers and prints the largest of the 3. 

a=input("Enter 1st Number: ")
b=input("Enter 2nd Number: ")
c=input("Enter 3rd Number: ")

if a>b:
    if a>c:
        print (a, " is the largest number!")
if b>a:
    if b>c:
        print (b," is the largest number!")
if c>a: 
    if c>b:
        print (c, " is the largest number!")


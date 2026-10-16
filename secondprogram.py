#Using escape line character
"""str1 = "This is my string.\nWe are creating it in python programming language"
print(str1)"""

#contatination
"""str1 = "Mahashakti "
#finding length of function
len1 = len(str1)
print(len1)

str2 = "Developers"
#finding length of function
len2 = len(str2)
print(len2)

final_str = str1 + str2
print(final_str)
print(len(final_str))"""

#Indexing
"""str = "Mahashakti developers"
ch = str[0]
ch1 = str[4]
ch2 = str[11]

print(ch)
print(ch1)
print(ch2)"""

#Slicing
"""str = "Aaditya vyas"
print(str[0 : 8])
print(str[  : 4])
print(str[1 :  ])"""

#Negetive slicing
"""str = "Lovie"
print(len(str))
print(str[-6 : ])
print(str[:-1])""" 


#string function 
"""str = "i am a coder, I am learning Machine learning"

str = str.capitalize() #it will work for every string because original string is modified

print(str.endswith("ege")) #(Gives answer in boolean values)
print(str.startswith("i")) #(Gives answer in boolean values)
print(str.capitalize()) #works only 1 time because it creates a new sting

print(str.replace("am learning", "have learned"))
print(str.find("machine")) 
print(str.count("am"))"""


#Practice question
#1
"""name = input("Enter first name: ")
print("Length of your name is" ,len(name))"""

#2
"""str = "Hi, $I am the $symbol $99.99"
print(str.count("$"))"""


#Conditional statement 
#if statement
# age = 18
"""age = input("Enter your age: ")

if age == 18:
    print("Can vote and applt for licence")
else:
    print("Can't vote and cannot apply for licence")"""


#Elif statement
"""light = "Green"

if(light == "Red"):
    print("Stop")
elif(light == "Green"):
    print("You can go")
elif(light == "Orange"):
    print("Wait, is turning red")"""

#using if statement multiple times
"""num = 7

if(num > 2):
    print("Greater than 2")
if(num > 3):
    print("Greater than 3")"""
#it will print both condition but if we use (if and else)it will print one condition


#else condition
"""light = "Pink"

if(light == "Red"):
    print("wait")
elif(light == "Green"):
    print("Go")
elif(light == "Orange"):
    print("wait is gonna be red")
else:
    print("Light is broken")"""


"""age = 27

if(age >= 18):
    print("Can vote")
else:
    print("Can't vote")"""


"""marks = int(input("Enter your marks: "))

if (marks >= 90):
    print("Grade A")
elif (marks >= 80):
    print("Grade B")
elif (marks >= 70):
    print("Grade C")
else:
    print("Grade D")

print("Grade of student is :",marks)"""



#Nesting
"""age = int(input("Enter your age: "))

if(age >= 18):
    if(age >= 80):
        print("Not eligible for driving")
    print("can drive")
else:
    print("Do not have licence,can't drive")"""



#Practice questions
#1
"""num = int(input("Enter a number: "))

if(num % 2 == 0):
    print("Number is EVEN")
else:
    print("Number is ODD")"""

#2
"""a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input ("Enter third number: "))
d = int(input("Enter Fourth number: "))

if(a >= b and a >=c ):
    print("\nFirst number is greatest",a)
elif(b >= c):
    print("\nSecond number is greatest",b)
elif(c >= d):
    print("\nThird number is greatest",c)
else:
    print(print("\nFourth number is greatest",d))"""

#3
""""num = int(input("Enter a number: "))

if(num % 7 == 0):
    print("Number is multiple of zero")
else:
    print("Number is not a multiple of zero")"""
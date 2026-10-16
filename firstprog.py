#------------------------CHARACTER SETS
"""
print("Hello, AV is my name") #printing values in same line by adding comma in between
print("MS51 is car business code") #printing values and numbers in same line
print(3106) #only numbers will be printed in the output
print(54-46) #it will print the difference of given input 
print(51+554) #it will print the sum of the given input
"""
#------------------------VARIABLES
"""
name = "Aadi"
age = 19
price = 29.99

age2 = age

print(name)
print(age)
print(price)

print("My name is:", name)
print("My age is:", age)
print("My price is:", price)

# (=)--> is called assignment operator

print(age2)
"""
#-----------------Data types (Integer, Float, string, Boolean, None)

#Used to print the type of varaible stored
"""
print(type(name))
print(type(age))
print(type(price))
"""
#-----------------Representation of string
"""
name1 = "AK"
name2 = 'AK'
name3 = '''AK'''

print(name1)
print(name2)
print(name3)
"""
#-----------------boolean
"""
age = 23
old  = True
a = None

print(type(old))
print(type(a))
"""
#-----------------question
"""SUM/DIFFERENCE
a = 31
b = 23
diff = a-b #a+b
print(diff)
"""

#-----------------arithmetic Operators
"""
a = 5
b = 8


print(a + b)#addition
print(a - b)#subtration
print(a / b)#division
print(a * b)#multiplication
print(a % b)#modulus -- used to find remainder
print(a ** b)#used to finf power of a^b
"""


#-----------------Relational Operators (returns boolean value)
"""
a = 50
b = 39

print(a == b)#False
print(a != b)#True
print(a >= b)#True
print(a > b)#True
print(a <= b)#False
print(a < b)#False
"""

#-----------------Assignment Operators
"""num = 20

#num += 10 #num = num + 10 both are same
#num -= 10
# num *= 10
# num /= 10
# num %= 10
# num **= 10

print("num :",num)
"""

#-----------------Logical Operators
""""
#1 not operator 
# print(not(True)) #returns False
# print(not(False))#returns True

a = 40
b = 30

print(not False)
print(not (a > b)"""

#2 and / or operator
"""val1 = True
val2 = True
print("AND operator: ", val1 and val2)

print("OR operator: ", val1 or val2)"""

"""a = 50
b = 20

val1 = True
val2 = False

print("AND operator: ", val1 and val2)
print("OR operator: ", (a == b) or(a > b))"""

#-----------------Type conversion 
#(Conversion = automatically)(Casting = manually)

#Type conversion
"""# a = int("20")
a  = float("20") #done by  type casting and only possible with numbers
b = 4.90

print(type(a))
print(a + b)"""

"""a = 3.14
a = str(a)

print(type(a))"""

#-----------------+Taking Input
"""name = input("Enter your name: ")
print("HEllO", name)"""

"""val = int(input("Enter some values: "))
print(type(val), val)"""

"""name = input("Enter your name: ")
age = int(input("Enter your age: "))
marks = float(input("Enter your marks: "))

print("welcome: ", name)
print("age: ",age)
print("marks: ",marks)"""

#-----------------Practice question
#1
"""num1 = int(input("enter number: "))
num2 = int(input("enter number: "))

print(num1 + num2)
print(num1 - num2)"""

#2
"""side = float(input("Enter square side: "))

print("area =", side * side)"""

#3
"""a = float(input("Enter first number: "))
b = float(input("Enter secong number: "))
print("avg = ",(a+b)/2)"""


#4
"""a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

print(a >= b)"""
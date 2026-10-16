#Loops
"""count = 1  #iterator
while count <= 10 :
    print("Hello")
    count += 1

print(count)"""

"""i = 1
while i <= 100:
    print("Hello",i)
    i += 1

print(i)"""

#print number from 1 to 41
"""i = 1
while i <= 41:
    print(i)
    i += 1

print("Loop ended")"""

"""i = 41
while i >= -41:
    print(i)
    i -= 1

print("loop ended")"""

#Practice question
# 1 (printing values positively)
"""num = 1
while num <= 100:
    print(num)
    num += 1"""

#2 (printing values negetively)
"""num = 100
while num >= 1:
    print(num)
    num -= 1"""

#3 Table of a number 
"""i =  1
while i <= 10:
    print(14 * i)
    i += 1"""

#table of any number by taking input from user
"""n = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(n * i)
    i += 1"""

#Travers (traveling one by one on each element in a loop)

# 4 (printing a number into loop)
"""nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1"""

#printing elements of a list into loop
"""team = ["Devang","Rohit","Jigar","Shobhit","rajat","deeptanshu","divyanshu"]

idx = 0
while idx < len(team):
    print(team[idx])
    idx += 1"""

# 5 (searching any specific number of list in a loop)
"""nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 81

i = 0
while i < len(nums):
    if(nums[i] == x):
        print("Found at idx", i)
    else:
        print("Finding")
    i += 1"""

#Break keyword (it terminates the running code when we add break condition)

"""i = 1
while i <= 31:
    print(i)
    if (i == 13):
        break
    i += 1

print("End of loop")"""

"""nums = (1, 4, 9, 16, 25, 31, 36, 49, 64, 81, 100)

x = 31

i = 0
while i < len(nums):
    if(nums[i] == x):
        print("Found at idx", i)
        break 
    else:
        print("Finding")
    i += 1

print("End of loop")"""


#Continue (It skips the iteration when we add continue condition and then again start executing )
"""i = 0 
while i <= 5:
    if (i == 3):
        i += 1
        continue
    print(i)
    i += 1 """

#prints odd numbers till 15 and skips even numbers
"""i = 1
while i <= 15:
    if (i%2 == 0):
        i += 1
        continue
    print(i)
    i += 1""" 

#prints even numbers and skips odd numbers till 15
"""i = 1
while i <= 15:
    if (i%2 != 0):
        i += 1
        continue
    print(i)
    i += 1 """


#For loop (used for sequential traversal ---->list,tuple,string)

#using for loop in list
"""nums = [1, 2, 3, 4, 5, 6]

for val in nums:
    print(val)"""


"""veggies = ["Tomato", "potato", "Ginger", "garlin", "onion"]

for elements in veggies:
    print(elements)"""

#using for loop in tuple
"""tup = (1, 2, 3, 4, 5, 6)

for num in tup:
    print(num)"""

#using for loop in str
"""str = "Mahashakti developers"

for char in str:
    print(str)
else:
    print("Pvt ltd")"""

"""str = "Mahashakti developers"

for char in str:
    if(char == 0):
        print("o is found")
        break
    print(char)

print("End of code")"""


#Practice questions
# 1
"""num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for elements in num:
    print(elements)"""

# 2
"""nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x = 81

idx = 0

or elements in nums:
    if(elements == x):
        print("Number found in idx",idx)
    idx += 1"""

#Range function()

# print(range(9))

"""seq = range(8)

for i in seq:
    print(i)"""

#type1
"""for i in range(31):   #range(stop)
    print(i)"""
#type2
"""for i in range(2, 10): #range(start, stop)
    print(i)"""
#type3
"""for i in range(2, 10, 2): #ramge(start, stop, step)
    print(i)"""


"""for i in range (2, 100, 2):
    print(i)"""

#Practice question
# 1
"""for i in range(1, 101):
    print(i)"""
#2 (step size can be negetive)
"""for i in range(100, 0, -1):
    print(i)"""
#3 table of any number using range function
"""num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num * i)"""
#4 printing even off numbers using range function
"""for i in range(40):

    if (i % 2 != 0): #even function
    if (i % 2 == 0): #off function
        print(i)"""

#Pass statememt (it's a null statement, used for future code)
"""for i in range(10):
    pass

print("Some usefull word done in future") #it will not get any error"""

#Practice question

# 1 (Total sum withwhile loop)
"""n = 10

sum = 0
for i in range(1, n+1):
    sum += i
    
print("Total sum =", sum)"""

# solving same by while loop
"""n = 7
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1

print("Total sum =", sum)"""

# 2(factorial using while loop)
"""n = 5
fact = 1
i = 1

while i <= n:
    fact *= i
    i += 1   

print("factorial =", fact)"""

# same program with while loop
"""n = 5
fact = 1

for i in range(1, n+1):
    fact *= i

print("Factorial is : " , fact)"""
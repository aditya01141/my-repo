#lists
""""Marks = [54.3, 58.4, 98.3, 88.4, 79.6, 89.5]
print(Marks)
print(type(Marks))
print(len(Marks))
print(Marks[0]) #Printing marks indexes
print(Marks[4])
print(Marks[5])"""


"""onar = ["Devang", 25, "Indore"]
print(onar)

onar[0] = "Rohit"
print(onar)"""

#Positive slicing
"""marks = [73.2, 96.4, 45.3, 88.3, 87.6, 79.3]
print(len(marks))
print (type(marks))
print(marks[0 : 2])
print(marks[3 : ])
print(marks[ : 6])"""

#Negetive slicing
"""marks = [73.2, 96.4, 45.3, 88.3, 87.6, 79.3]
print(marks[0 : -2])
print(marks[-3 : ])
print(marks[ : -5])"""


# Methods of lists
"""list = [1,2,9,4,7]

list.append(9)
print(list)

list.sort()
print(list)

list.sort(reverse = True)
print(list)

list.reverse()
print(list)

list.insert(0, 65)
print(list)

print(len(list))

list.remove(9)
print(list)

list.append(6)
print(list)

list.sort
print(list)

list.pop(3)
print(list)"""


#Tuple
"""tup = (3, 5, 6, 2, 8, 6, 4)
print(len(tup))
print(type(tup))"""

#Printing empty tuple
"""tup = ()
print(tup)
print(len(tup))
print(type(tup))"""

#Single value tuple (We can treat in different types, but if we add{,}after any element so i will act as tuple)
"""tup = (1,)
print(tup)
print(len(tup))"""

"""tup = (1.0)
print(tup)
print(type(tup))"""

#Tuple method
"""tup = (1, 2, 4, 5, 6, 9) #This helps to find the position of any number in the tuple
print(tup.index(4))
print(tup.count(1)) #used in counting the number from the tuple """


#Practice questions 
# 1
"""movies = []
mov = input("Enter 1st movie name: ")
movies.append(mov)
mov2 = input("Enter 2nd movie name: ")
mov3 = input("Enter 3rd movie name: ")

movies.append(mov2)
movies.append(mov3)

print(movies)"""

#2
"""list1 = [2, 4, 2]
list2 = [2, 4, 5]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("List is palindrome")
else:
    print("Not a palindrome")"""
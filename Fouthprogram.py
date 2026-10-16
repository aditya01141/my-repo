#Dictonary
"""info = {
    "Name" : "Devang",
    "Car" : "Fortuner",
    "Business" : "MV41",
    "Locality" : "Indore",
    "Age" : 25,
    "is_adult" : True,
    "Income" : 35.85 ,
}

print(info)
print(len(info))
print(type(info))

print(info["Name"])
print(info["Business"])
print(info["Income"])

info["Name"] = "Yadav"
info["Car"] = "Legender"
info["Income"] = "Crore"

print(info)"""


# Nested dictonary
"""student = {
    "name" : "Aaditya vyas",
    "subjects" : {                  #individual dict can also be printd
        "Physics" : 77,
        "Maths" : 88,
        "C progamming" : 99,
    }
}

print(student)"""

# Dictonary method
"""info = {
    "Name" : "Devang",
    "Car" : "Fortuner",
    "Business" : "MV41",
    "Locality" : "Indore",
    "Age" : 25,
    "is_adult" : True,
    "Income" : 35.85 ,
}

print(info)

print(info.keys())
print(list(info.values()))
print(list(info.items())) #Printed in the form of tuple

#accessing individually (returns all key and values paris as tuples)
pairs = list(info.items())
print(pairs[0])
print(pairs[1])
print(pairs[2])
print(pairs[3])

#both will return same values 
print(info["Name"])      #if keys gets incorrect it will return error
print(info.get("Name"))  #if keys gets incorrect it will return none

info.update({"car_type" : "Disel"})
print(info)
#or
new_dict = ({"car_type" : "Disel"})
info.update(new_dict)

print(info)"""


#Sets (it's unordered pair)
"""# collection = {1, 2, 3, 4, 5, 6}
collection = {1, 2 , 3, 4, "Adi", "Yaar"} #if we add same values multiple times, then set ignores duplicate values 

print(collection)
print(type(collection))
print(len(collection))   #(it'll not print duplicate values """

#Empty set syntax
"""collection = set()
print(type(collection))
print(len(collection))"""

#Set method
"""set = {1, 4, 2, 6, 9, 8}
set.add(8)
print(set)

set.remove(4)
print(set)

set.pop() #removes random value
print(set)

set.clear()
print(set)
print(len(set))"""

#pop method
"""collection = {"Hello", "Aadi", "Lovieee", "Mackbook"}

print(collection.pop())
print(collection.pop())
print(collection.pop())"""

#set union ----> (combines sets and return new values by  not returning repeated values)
"""set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2)) 

#if we print old sets it will print original sets , it'll not change sets
print(set1)
print(set2)"""

#Set intersection ---->(returns only common values)
"""set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.intersection(set2))"""

#Practice questions
# 1
"""dict = {
    "cat" : "a small animal",
    "table" : ["A piece of furniture","list of facts and figures"]
}
print(dict)"""

# 2
"""subjects = {
    "python", "java", "c++", "c", "javascript", "java",
    "python", "java", "c++", "c"
}
print(subjects)
print(len(subjects))"""

# 3
"""marks = {}

x = int(input("Enter physics: "))
marks.update({"physics": x}) 

x = int(input("Enter chemistry: "))
marks.update({"chemistry": x}) 

x = int(input("Enter math: "))
marks.update({"math": x})

print(marks)"""

# 4
"""values = {
    ("float",99.0),
    ("int",99)
}
print(values)"""
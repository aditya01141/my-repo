#Open I/O
"""f = open("demo.txt", "r")     #opening a file

data = f.read()              #reading a file
print(data)                  #printing the data of file and also type of data
print(type(data))

f.close"""                       #closing the file


"""Important character of file I/O
1. "r" open for reading
2. "w" open for writing 
3. "x" create a new file and open for writing
4. "a" open for writing, appending to enf of file if exists
5. "b" binary mode
6. "t" text mode
7. "+" open a disk file for updating
"""


"""Methods for Reading a file
1. f.read() -----> reads entire file
2. f.readline() -----> reads onw line at a time
"""

"""f = open("demo.txt", "r")

data = f.read(6)     #used to print specified numbers of characters
print(data)

f.close"""


"""f = open("demo.txt", "r")

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

# line3 = f.readline()           #it will be printed empty if we don't have data in next line
# print(line3)

f.close()"""


#Writing to a file
#Method overriting (writing)
"""f = open("demo.txt", "w")

f.write("I want study and learn about machine learning")

f.close
"""

#method of appending
"""f = open("demo.txt", "a")

f.write("\nThen i'll move to java script or react js")

f.close"""

#opening a sample while which current do not exist

"""f = open("Sample.txt", "w")
f.close()"""
# the file will exist in w and a mode

#opening file with (r+) mode (it'll overwrite in the starting of the line)
"""f = open("demo.txt", "r+")
data = f.readline()
print(data)
f.write("ABC")"""


#Modes
"""1. "r" - open for reading
2. "w" - open for writing
3. "a" - open for writing but adds at the end of file 
4. "b" - binary mode
5. "r+" - read + overrights (prints in the starting) no truncate
6. "w+" - read + overrights (truncate)"""


#With syntax
"""with open ("demo.txt", "r") as f:
    data  = f.read()
    print(data)"""


"""with open ("demo.txt", "w") as f:
    f.write("new data")"""

#deleting a file
"""import os
os.remove("practice.txt")"""


#Practice question
# 1
"""with open("practice.txt", "w") as f:
    f.write("Hi everyone\nwe are leaning file I/O\n")
    f.write("Using java.\nI like programming in java.")"""

# 2
"""with open("practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("java", "Python")
print(new_data)

with open("practice.txt", "w") as f:
    f.write(new_data)"""

# 3 
"""def check_for_word():
    word = "learning"
    with open("practice.txt", "r") as f:
        data = f.read()
        if (data.find(word) != -1):
            print("Found")
        else:
            print("Not found")

check_for_word()"""

# 4
"""def check_for_word():
    word = "learning"
    with open("practice.txt", "r") as f:
        data = f.read()
        if (word in data):
            print("Found")
        else:
            print("Not found")

def check_for_line():
    word = "programming"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data  = f.readline()
            if (word in data):
                print(line_no)
                return
            line_no += 1
    return -1

check_for_line()"""

# 5
#without seperator
""" with open("practice.txt", "r") as f:
    data = f.read()
    print(data)

    num = ""
    for i in range(len(data)):
        if(data[i] == ","):
            print(int(num))
            num = ""
        else:
            num += data[i]"""


# with seperator
"""count = 0
with open("practice.txt", "r") as f:
    data = f.read()

    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1

print(count)"""
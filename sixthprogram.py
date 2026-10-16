#Functions (used for reducing redendency {repetations} in the code)

#function defination
"""def calc_sum(a,b):     
    sum = a + b
    print(sum)
    return sum

calc_sum(31, 23)

# some lines of codes

calc_sum(29,48)

# some lines of codes

calc_sum(33, 93)"""



#easy method
"""def calc_sum(a, b):         #these are called paremeter
    return a + b

sum = calc_sum (2, 49)     #function call; argumwnts
print(sum)"""



"""def print_say_hiilovieee():
    print("Hello cutieeee")


print_say_hiilovieee()"""


#avg calculation function
"""def print_avg(a, b, c):
    sum = a + b + c
    avg = sum / 3
    print(avg)
    return avg

print_avg(24, 94, 43)"""

#Types of functions
"""1 Built-in function
print()
len()
type()
range()"""

# 2 User defined function


#Default parameter
"""def calc_prod(a=1, b=1):       #here we have given 1 as default value in both parameter
    print(a * b)
    return(a * b)

calc_prod()"""

#Practice question
# 1
"""cities = ["delhi", "bhopal", "indore", "Dewas", "ujjain"]
heroes = ["Jigar", "Devang", "Rohit", "Shobhit"]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)"""

# 2
# it will print whole list in a line
"""cities = ["delhi", "bhopal", "indore", "Dewas", "ujjain"]

def print_len(list):
    print(len(list))

def print_list(list):
    for item in list:
        print(item, end =" ")

print_list(cities)
print()"""

# 3
"""def cal_fact(n):
    fact = 1
    for i in range (1, n+1):
         fact *= i

    print(fact)

cal_fact(5)"""


#4
# Doller conversion
"""def converter(usd_val):
    inr_val = usd_val * 83

    print(usd_val, "USD = ", inr_val, "INR")

converter(23)"""

# 5
"""def check_even_odd(num):
    if num % 2 == 0:
        print("Number is even: ", num)
    else:
        print("Number is odd: ", num)

number = int(input("Enter a number : "))

check_even_odd(number)"""

#Recusrsion  (advance version of loop)
"""def show(n):
    if(n == 0):  #called as base case
        return
    print(n)
    show(n-1)

show(40)"""

#steps to solve recursive problem
# 1 kaam dekhte hai kakya karwwana hai uske badh dekhte hai base case kya hona chahiye 

#Recrence relation------------>  [n!= (n - 1)! * n]

#Recursion through factorial
#To calculate fact of any number we can calculate (n-1) and then multiply with (n)

"""def fact (n):
    if(n == 1 or n == 0):
        return 1
    return fact(n-1) * n


print(fact(8))"""

# Practice question
# 1
"""def calc_sum(n):
    if (n == 0):
        return 0
    return calc_sum(n-1) + n


sum = calc_sum(9)
print(sum)"""

# 2
"""def print_list(list, idx = 0):
    if(idx == len(list)):
        return
    
    print(list[idx])
    print_list(list, idx+1)

fruits = ["Mango", "Apple", "Litchi", "Banana", "kiwi"]
print_list(fruits)"""
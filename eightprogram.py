#OOPS  
#Creating a student class with object and class

"""class student:              #--> class
    name = "Devang"

s1 = student()                #--> object
print(s1.name)

s2 = student()
print(s2.name)"""

"""class car:
    colour = "black"
    brand = "Mahindra"
    model = "Scorpio N"

car1 = car
print(car1.colour)
print(car1.brand)
print(car1.model)"""

#Constructor (__inti__ function)  invokes at the time of exectution
#attributes = data; variables

""""class student:
    # name = "Devang"
    def __init__ (self, fullname, Mycar):
        self.name = fullname
        self.car = Mycar
        print("Adding new students in the data base ")

s1 = student("Devang", "Fortuner")
print(s1.name)
print(s1.car)

s2 = student("Jigar", "Scorpio N")
print(s2.name)
print(s2.car)"""

#Default perameter
"""class student:
    collage_name  = "Medicaps university"
    #default perameter
    def __init__ (self):
            pass

    #perameterized perameter
    def __init__ (self, fullname, Mycar):
        self.name = fullname
        self.car = Mycar
        print("Adding new students in the data base ")

s1 = student("Devang", "Fortuner")
print(s1.name, s1.car)

s2 = student("Jigar", "Scorpio N")
print(s2.name, s2.car)

print(s2.collage_name)"""



#object attribute > class attribute
"""class student:
    collage_name  = "Medicaps university"
    name = "Annoymous"      #class attribute

    def __init__ (self, fullname, Mycar):
        self.name = fullname       #object attribute
        self.car = Mycar
        print("Adding new students in the data base ")

s1 = student("Devang", "Fortuner")
print(s1.name)"""


#def perameter
"""class student:
    collage_name = "Medicaps university"

    def __init__(self, fullname, Mycar):
        self.name = fullname
        self.car = Mycar

    def welcome(self):
        print("welcome students", self.name)

    def car_info(self):
        return self.car

s1 = student("Devang", "Fortuner legender")
s1.welcome()
print(s1.car_info())"""


#Practice question
# 1
"""class student :
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calc_avg (self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi", self.name, "Your avg score is: ", sum/3 )

s1 = student("Jatin", [77, 80, 99])
s1.calc_avg()
s2 = student("Aarjav", [83, 77, 99])
s2.calc_avg()
s3 = student("Devansh", [99, 88, 67])
s3.calc_avg()

#changing attribute value directly
s1.name = "Aaditya"
s1.calc_avg()"""


#Static methods (which do not use self perimeter ) These methods are at class level
"""class student:
    # name = "Devang"
    def __init__ (self, fullname, Mycar):
        self.name = fullname
        self.car = Mycar

    @staticmethod       #This is a decorator
    def collage():
        print("Medicaps university")

s1 = student("Devang", "Fortuner")
print(s1.name)
print(s1.car)"""


#Abstration ---> means hiding unnessary details from the user for a program
"""class car :
    def __inti__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("Car started")

car1 = car()
car1.start()"""

#The unnessary details are hidden from the user basically the steps
# and the final process is been executed


#Encapsulation ---> wrapping data and functions into a single unit (object)


#Practice question
# 1
"""class Bank_account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_number = acc

    #debit method
    def debit(self, amount):
        self.balance -= amount
        print("RS:", amount, "Was debited")
        print("~ Total balance :", self.get_balance())


    def credit(self, amount):
        self.balance += amount
        print("RS:", amount, "Was credited")
        print("~ Total balance :", self.get_balance())


    def get_balance(self):
        return self.balance


acc1 = Bank_account(10000000, 456225)
# print(acc1.balance)
# print(acc1.account_number)


acc1.debit(4575)
acc1.credit(51000)
acc1.debit(200000)
acc1.credit(750000)
print(acc1.balance)"""
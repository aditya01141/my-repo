#DEL keyword
"""class student:
    def __init__(self, name):
        self.name = name

s1 = student("Akkshadha")
print(s1.name)

del s1.name
print(s1.name)"""

#Private (like) attribute and methods
# if we want to keep something private so by adding double(__) it will not be printed pr accessed by anybody
"""class account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass


acc1 = account("3422342", "harish")

print(acc1.acc_no)
print(acc1.acc_pass)"""


"""class person:
    __name = "Anonymous"

    def __hello(self):
        print("hello person!")

    def welcome(self):
        self.__hello()

p1 = person()

print(p1.welcome())"""

#Inheritance

#Single inheritance (it has single parent class and single child class)
"""class car:
    color = "White"

    @staticmethod
    def start():
        print("Car started...")


    @staticmethod
    def stop():
        print ("Car stopped...")

class Toyotacar(car):
    def __init__(self, name):
        self.name = name

car1 = Toyotacar("Fortuner leader ")
car2 = Toyotacar("Fortuner legender 4*4")


car1.start()
print(car1.color)
print(car1.name)
print(car2.name)"""


#Multi level inheritance (has two parent class one is grandparent and another is parent and single child class)
"""class car:

    @staticmethod
    def start():
        print("Car started...")


    @staticmethod
    def stop():
        print ("Car stopped...")

class Toyotacar(car):
    def __init__(self, brand):
        self.brand = brand

class Fortuner(Toyotacar):
    def __init__(self, brand, car_name, fuel_type, milage):
        super(). __init__(brand)           ---> super method is used to access methods of parent class
        self.car_name = car_name
        self.fuel_type = fuel_type
        self.milage = milage


car1 = Fortuner("Toyota","Fotuner", "Diesel", 14 )

car1.start()
print("Brand:", car1.brand)
print("Car name: ", car1.car_name)
print("Fuel_type: ", car1.fuel_type)
print("Milage: ", car1.milage)"""

#Multiple inheritance (has 2 differnt parent class and single derived child class)
"""class A:
    varA = "Welcome to class A"

class B:
    varB = "Welcome to class B"

class C(A, B):
    varC = "Welcome to class C"

c1 = C()

print(c1.varC)
print(c1.varB)
print(c1.varA)"""


# Super method (super method is used to access methods of parent class)
""""class car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stoped")

class toyotacar(car):
        def __init__(self, name, type):
            super(). __init__(type)         #>>>super method called 
            self.name = name
            super().start()

car1 = toyotacar("Legender", "Neodrive")
print("Car type: ", car1.type)
print("Car name: ",  car1.name)"""


#Class method
"""class person:
    name = "Annoymous"

    def changename(self, name):
        self.__class__.name = "Jigar0051" #this will also print same output
        # self.name = name    >>>this will note change class attribute it will create new
        person.name = name

p1 = person()
p1.changename("Jigar0051")
print(p1.name)
print(person.name) #now class attribute is changed on both places"""


# but to change anything directly we can use class method
"""class person:
    name = "Annoymous"

    @classmethod     #this function returned better function which updated directly class attribute
    def changename(cls, name):
        cls.name = name

p1 = person()
p1.changename("Jigar0051")
print(p1.name)
print(person.name)"""


#Types of methods in inheritance 
# 1 static method ---> which do not change or access instance or attribute
# 2 class methods ---> which has cls as 1st implisit argument
# 3 instance methods ---> which has self as 1st implisit argument


#property decorator
"""class student:
    def __init__(self, phy, math, chem):
        self.phy = phy
        self.math = math
        self.chem = chem

        # self.percentage = str((self.phy + self.math + self.chem) / 3) + "%"

    # def calcpercentage(self):
        # self.percentage = str((self.phy + self.math + self.chem) / 3) + "%"

        #using property decortor
    @property
    def percentage(self):
        return  str((self.phy + self.math + self.chem) / 3) + "%"

stu1 = student(93, 84, 86)
print(stu1.percentage)

stu1.phy = 66
print(stu1.percentage)"""


#Polymorphism (operator overloading)
# (when the same operator is allowed to have different meaning according to the context)


"""print(41 + 51) #3
# print(type(41))
print("Akkshadha" + "rathore") #concatinate
# print(type("akkshadha"))
print(([23,34,54,34] + [34,65,23,35])) #merge"""

"""class complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def shownumber(self):
        print(self.real,"i", self.img,"j")

    #Dunder addition function
    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return complex(newReal, newImg)

        #Dunder subtraction function
    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return complex(newReal, newImg)

num1 = complex(34, 56)
num1.shownumber()

num2 = complex(47, 84)
num2.shownumber()

num3 = num1 + num2
num3.shownumber()

num4 = num1 - num2
num4.shownumber()"""


#Practice question
#1
"""class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (22/7) * self.radius ** 2

    def perimeter(self):
        return 2 * (22/7) *  self.radius

c1 = circle(21)
print(c1.area())
print(c1.perimeter())"""

#2
"""class employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showdetails (self):
        print("Role =", self.role)
        print("Dept =", self.dept)
        print("Salary =", self.salary)

class engineer(employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age 
        super().__init__("Software_engineer", "IT", "620,000")

e1 = employee("Chartered accountant", "finance", "120,000")
e1.showdetails()

engg1 = engineer("Jigar", 20)
engg1.showdetails()"""

"""File handling in python"""



"""reading a file in python """

# ayush = open("ayush.txt", "r")
# content = ayush.read()
# print(content)
# ayush.close()







"""writing a file in python """

# ayush = open("ayush.txt", "w")
# ayush.write("""
# ayush is a good coder.
# He loves to solve problems.
# He is learning Python.
# """)
# ayush.close()


"""Doing both reading and writing a file in python """

# ayush = open("ayush.txt", "w")
# ayush.write("""
#             Ayush is a boy.
#             He loves coding.
#             He is learning Python.
#             he is 18 years old.""")

# ayush = open("ayush.txt", "r")
# content = ayush.read()

# print(content)
# ayush.close()


"""doing python coding in different file and reading it in another file"""

# ayush = open('test.py', 'w')
# ayush.write("""# this is a test file\nprint("Hello, World!")\n

# print("Hello, World!")
# num1 = int(input())
# num2 = int(input())
# sum = num1 + num2   
# print("The sum is:", sum)
# """)

# ayush.close()

"""creating and reading a new file in python"""


# new = open("new.txt", "x")
# new.write("This is a new file created by Ayush.")
# new.close()
# new = open("new.txt", "r")
# print(new.read())
# new.close()'



"""__________________________________________________________________________________________________________________"""



"""learning classes in python"""

# class Ayush :
#     x = 5
#     y = 10
    
#     summ = x + y
#     pass
# object1 = Ayush()
# print(object1.summ)

"""using __init__ method of class in python"""

# class person:
#     def __init__(self,name,age,city):
#         self.name = name
#         self.age = age  
#         self.city = city
# obj = person("ayush", 18,"gurugram")
# print(obj.name)
# print(obj.age)
# print(obj.city)


"""Self parameter in python class"""

# class person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def greet(self):
#         print(f"hello sir {self.name} we are welcoming you here")

# obj = person("ayush", 18)

# obj.greet()



"""Making a car information using from car name with class in python"""

# class car:
#     def __init__(self,company,model,year,price):
#         self.company = company
#         self.model = model
#         self.year = year
#         self.price = price
#     def car_info(self):
#         print(f"""
#         company of car is : {self.company}
#         model of car is : {self.model}
#         year of car is : {self.year}
#         price of car is : {self.price}
#         """)

# car_obj1 = car("lexus","RX 500h",2024,9000000)
# car_obj2 = car("BMW","X5",2024,8500000)
# car_obj3 = car("audi","Q7",2024,8000000)

# car_name = input("Enter the car company name: ")
# if car_name.lower() =="lexus":
#     car_obj1.car_info()
# elif car_name.lower() =="bmw":
#     car_obj2.car_info()
# elif car_name.lower() =="audi": 
#     car_obj3.car_info()
# else:
#     print("cruntly not in stock")





"""Student Performance Evaluation System using Python Classes"""

# class Student:
#     def __init__(self,name ,roll_number,marks):
#         self.name = name
#         self.roll_number = roll_number
#         self.marks = marks

#     def average(self):
#         if not self.marks:
#             return 0
#         return sum(self.marks)/len(self.marks)

#     def grade(self):
#         avg = self.average()
#         if avg >= 90:
#             return "A"
#         elif avg >= 80:
#             return "B"
#         elif avg >= 70:
#             return "C"
#         elif avg >= 60:
#             return "D"
#         else:
#             return "Fail"
# student1 = Student("Ayush", 101, [85, 90, 78, 92, 88])
# print(f"student name: {student1.name}")
# print(f"roll number: {student1.roll_number}")
# print(f"average marks: {student1.average()}")
# print(f"grade: {student1.grade()}")


"""__________________________________________________________________________________________________________________"""

# class house:
#     def __init__(self,bill,length, breadth,electric_units,house_price):
#         self.bill = bill
#         self.length = length
#         self.breadth = breadth
#         self.electric_units = electric_units
#         self.house_price = house_price
#     def area(self,area):
#         area = self.length * self.breadth
#         return area
#     def house_price(self,house_price):
#         house_price = 10000 * self.area(0)
#         return house_price
#     def total_bill(self,total_bill):
#         total_bill = self.bill + (self.electric_units * 7)
#         return total_bill
# house_obj = house(5000, 50, 40, 150)
# house_obj2 = house(6000, 60, 50, 200)
# print(f"Area of house is : {house_obj.area(0)} sq ft")
# print(f"Total bill of house is : {house_obj.total_bill(0)} rs")

# print(f"Area of house is : {house_obj2.area(0)} sq ft")

# ayush = open("new_file.py" ,  "x")
# ayush.write("""print("This is a new python file created by Ayush")
#                 a = int(input())
#                 b = int(input())
#                 summ = a + b
#                 print(f"the sum is : {summ}")

            
#                 """)
# ayush.close()
 



"""making a new class """

# class new_class:
#     def __init__(self,name,reg_no):
#         self.name = name
#         self.reg_no = reg_no

# ayush = new_class("ayush", 251356004)
# print(ayush.name)        




# class classes:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         pass
# object1 = classes("Ayush",18)

# print(object1.name)



# class ayush:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# ayush_object = ayush("Ayush",123)
# print(ayush_object.name)


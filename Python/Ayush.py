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

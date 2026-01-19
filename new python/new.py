print("hello i am making a calculator with def function ")


num1 = int(input("enter first number here : "))
num2 = int(input("enter secound number here : "))
operation = input("tell the operation which i have to operate : ")
def add(num1,num2,final_result):
    final_result = num1 + num2
    print(f"addition of num1 and num2 is : {final_result}")
def sub(num1,num2,final_result):
    final_result = num1 - num2
    print(f"addition of num1 and num2 is : {final_result}")
if operation == "+":
    print(add())
elif operation == "-":
    print(sub())

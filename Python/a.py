# a = int(input())
# arr = list(map(int, input().split()))
# tar = int(input(""))
# start = 0
# end = a-1
# answer = -1
# while start <= end:
#     mid = (start + end)//2
#     if tar == arr[mid]:
#         answer = mid
#         break
#     elif tar > arr[mid]:
#         start = mid + 1
#     else:
#         end=mid-1
# print(answer)
# print(a*10)
        




# a = int(input())
# arr1 = []
# for i in range(a):
#     arr2 = list(map(int, input().split()))
#     arr1.append(arr2)
# summ = 0
# for i in range(a):
#     for j in range(a):
#         if i == 0 or j == 0 or i == a-1 or j ==a-1:
#             summ += arr1[i][j]
# print(f"Sum of border elements: {summ}")



# string
# number float, int, complex
# num1 = int(input())
# num2 = int(input())
# num3 = int(input())

# avg = ( num1+num2+num3)/3
# print(avg)

# a, b,c = map(int,input().split())
# avg = (a+b+c)/3
# print(avg)
# a = str(input())
# b = str(input())

# print(a+b)

# x, y ,z= input("Enter two numbers: ").split()
# x = int(x)
# y = int(y)
# z = int(z)

# avg = float((x+y+z)/3)
# print(x+y)
# # print("ayush" , x+y)
# print(f"ayush {avg:.10f}")

# a = int(input())
# if a >= 18:
#     a -= 5
#     print(a)
# else:
#     print("you are ayush")
# a = "ayush"
# a = a[-1]
# print(a)
# a = "ayush"
# print(f"the last value is : {a[-1]}")

# a = "ayush"
# print(f"the forth letter is: {a[3]}")

# a = int(input(""))
# # a = a**5
# print(f"{a**3}")
# a ,b = map(int,input().split())

# c = a-b
# print(c)
# if a > b:
#     print(f"this is the difference : {a-b}")
# else:
    
#     print(f"this is the diffence : {b-a}")
# def asd(a,b):
#     if a >= b:
#         return a-b
#     else:
#         return b-a
# result = asd(a,b)
# print(result)

# Use print() to print to the console
# a = float(input())
# b = float(input())
# c = int((a%1)*10)
# d = int((b%1)*10)

# if c > d:
#     print(c)
# else:
#     print(d)



# Use print() to print to the console
# a,b,c,d = map(int, input().split())
# maxx = max(a,b,c,d)
# print(maxx)

# for i in range(5, 0, -1):

#     print(i)





#use while loop
# totle = 0
# while  True:
#     x = int(input())
#     if x ==0:
#         break
#     totle = totle + x
# print(totle)
# print("Input any number!")
# a = int(input())
# arr = []
# summ = 0
# for i in range(a):
#     print("input: ",i)
#     x = int(input())
#     arr.append(x)

# for j in arr:
#     summ += j

# print("Sum of rray is: ",summ)



# n = int(input())

# n = int(input("enter a number : "))
# print(f"square: {n**2}")
# print(f"cube: {n**3}")
# print(f"cube root: {n**0.333 :.2f}")
# print(f"square root: {n**0.5 :.2f}")

# p,r,t = map(int,input().split())
# m=(p*r*t)/100
# print(m)
# print(f"{m:.0f}")

# a, b = map(int , input().split())
# print(f" perimeter : {a*b}")

# c,d = map(int, input().split())
# print(f" sum: {c+d}")
# print(f" subtract: {c-d}")
# print(f" multiply: {c*d}")
# print(f" divide: {c/d}")

# a = [1,3,4,67,8,8]
# print(a[2])



# n = int(input())
# arr = list(map(int, input().split()))
# count = 0
# for i in range(len(arr)):
#     prime = True
#     for j in range(2,arr[i]):
#         if arr[i]%j == 0:
#             prime = False

#             break
#     if prime == True:
#         print(f"prime number: {arr[i]}")
#         count += 1
# print(count)


# arr = list(map(int, input().split()))
# maxx = max(arr)
# minn = min(arr)

# max_index =  arr.index(maxx)
# min_index = arr.index(minn)

# arr[max_index] , arr[min_index] = arr[min_index] , arr[max_index]
# print(* arr)

# a = int(input())
# arr = list(map(int,input()))
# b = int(input())
# c = arr.index(b)
# print(c)

# a = input()
# print(f"Length : {len(a)}")
# print(f"Secret Code : {a[5:15]}")
# print(f"Uppercase: {a.upper()}")
# print(f"Recersed Message: {a[::-1]}")



# my_list = [1, 2, 3]
# for v in range(len(my_list)):
#     my_list.insert(1, my_list[v])
# print(my_list)

# my_list_1 = [1, 2, 3]
# my_list_2 = []
# for v in my_list_1:
#     my_list_2.insert(0, v)
# print(my_list_2)


# tup = (1, 2, 4, 8)
# tup = tup[1:-1]
# tup = tup[0]
# print(tup)

# my_list = [1, 2]

# for v in range(2):
#     my_list.insert(-1, my_list[v])

# print(my_list)


# def function_1(a):
#     return None


# def function_2(a):
#     return function_1(a) * function_1(a)


# print(function_2(2))

# my_list =  [x * x for x in range(5)]


# def fun(lst):
#     del lst[lst[2]]
#     return lst


# print(fun(my_list))

# x = 1
# y = 2
# x, y, z = x, x, y
# z, y, z = x, y, z

# print(x, y, z)


# x = int(input())
# y = int(input())
# x = x % y
# x = x % y
# y = y % x
# print(y)

# dct = {'one': 'two', 'three': 'one', 'two': 'three'}
# v = dct['three']

# for k in range(len(dct)):
#     v = dct[v]

# print(v)
# def fun(x, y):
#     if x == y:
#         return x
#     else:
#         return fun(x, y-1)


# print(fun(0, 3))

# i = 0
# while i < i + 2 :
#     i += 1
#     print("*")
# else:
#     print("*")


# dct = {}
# dct['1'] = (1, 2)
# dct['2'] = (2, 1)

# for x in dct.keys():
#     print(dct[x][1], end="")

# def fun(inp=2, out=3):
#     return inp * out


# print(fun(out=2))


# lst = [[x for x in range(3)] for y in range(3)]

# for r in range(3):
#     for c in range(3):
#         if lst[r][c] % 2 != 0:
#             print("#")


# try:
#     value = input("Enter a value: ")
#     print(int(value)/len(value))
# except ValueError:
#     print("Bad input...")
# except ZeroDivisionError:
#     print("Very bad input...")
# except TypeError:
#     print("Very very bad input...")
# except:
#     print("Booo!")

foo = (1, 2, 3)
a = foo.index(0)
print(a)

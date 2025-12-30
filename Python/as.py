# # Use print() to print to the console
# n = int(input(""))
# arr = list(map(int,input().split()))

# for i in range(len(arr)):
#     if arr[i]%2 == 0:
#         a = "E"
#     else:
#         a = "O"
# print(a)

# arr = [1,2,4,5,6,7,7,8,4,6,3,2]
# # arr[3] = 10
# # mid2 = len(arr)//2 
# # mid1 = mid2 -1
# # print(f"our first mid number is : {arr[mid1]} and secound mid number is {arr[mid2]}")
# for i in arr:
#     if i % 2 ==0:
#         print(f"even number : {i}")
       
#     elif i % 2 != 0:
#         print(f"odd number : {i}")



# n = int(input())
# arr = list(map(int, input().split()))
# summ = 0
# for i in range(len(arr)):
#     count = 0
#     for j in range(len(arr)):
#         if arr[i] == arr[j]:
#             count += 1
    
#     if count == 1:
#         summ += arr[i]
# print(summ)

# n = int(input())
# arr = list(map(int, input().split()))
# #[4 ,6754]
# for i in range(len(arr)):
#     prime = True
#     for j in range(2,arr[i]):
#         if arr[i] % j == 0:
#             prime = False
#             break
#     if prime == True:
#         print(f"prime number is : {arr[i]}")
#     else:
#         print("Not Prime")
    


# n = int(input())
# arr = list(map(int, input().split()))
# summ = 0
# for i in range(len(arr)):
#     count = 0
#     for j in range(len(arr)):
#         if arr[i] == arr[j]:
#             count +=1
#     if count == 1:
#         summ += arr[i]
# print(summ)

# n = int(input())
# arr = list(map(int,input().split()))
# for i in range(len(arr)):
#     prime = True
#     for j in range(2,arr[i]):
#         if arr[i]%j ==0:
#             prime =False
#     if prime == True:
#         print(f"prime number : {arr[i]}")    
#     else:
#         print(f"not prime:{arr[i]}")

# n = int(input())
# arr = list(map(int,input().split()))
# summ = 0 
# for i in range(len(arr)):
#     count = 0
#     for j in range(len(arr)):
#         if arr[i] == arr[j]:
#             count += 1
#     if count == 1:
#         summ += arr[i]
# print(summ)


# n = int(input())
# arr = list(map(int, input().split()))


a = "hello "
# b = a * 3
# print(b)
print(a * 3)

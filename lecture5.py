# i = 1
# while i <= 100 :
#     print(i)
#     i += 1
# i = 100
# while i >= 1:
#     print(i)
#     i -= 1
# i = 1
# while i <= 10:
#     print(6*i)
#     i += 1
# list = [5, 7, 3, 8, 1, 9]
# i = 0
# while i < len(list):
#     print(list[i])
#     i += 1
# tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# i = 0
# x = 64 #jab hume koi specific find karna ho toh aise karenge
# while i < len(tup):
#     if(tup[i] == x):
#         print("found at index", i)
#     i += 1    
# i = 0
# while i <= 5:
#     if(i == 3):
#         i += 1
#         continue
#     print(i)
#     i += 1
# i = 0
# while i <= 10:
#     if(i%2 != 0):
#         i += 1
#         continue
#     print(i)
#     i += 1

# list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# for val in list:
#     print(val)
# list = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49)
# idx = 0
# for el in list:
#     if(el == 49):
#         print("found at index:", idx)
#     idx += 1    

# for i in range(5):    #(stop value)
#     print(i)

# for i in range(2,10):    #(start value,stop value)
#     print(i)

# for i in range(2,10,2):   #\(start value, stop value, step value) step value matlab kitna ka gap chhaiye   
#     print(i)
# for i in range(2,101,2):    #even no print
#     print(i)
# 
# for i in range(1,101,2):       #odd no print
#     print(i)
# n = int(input("enter number: "))    #table print with while loop
# i = 1
# while i <= 10:
#     print(n*i)
#     i += 1
# n = int(input("enter no: "))        #table with for loop 
# for i in range(1,11):   
#     print(n*i)
# n = int(input("enter no : "))         #sum of n numbers
# sum = 0
# for i in range(n+1):
#     sum += i
# print("total sum =", sum)    
# n = int(input("enter no: "))     #sum n number with while loop
# sum = 0  
# while n >= 1:
#     sum += n
#     n -= 1
# print("total sum: ", sum)    
n = int(input("enter no: "))
fact = 1
for i in range(1,n+1):
    fact *= i
print("factotial :", fact)    
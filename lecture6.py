# def calcsum(a, b):
#     sum = a + b
#     print(sum)

# calcsum(890, 4)
# def nullprint():
#     print("hello world")

# out = nullprint()
# print(out)

# def avgof5(a,b,c,d,f):
#     sum = a+b+c+d+f
#     avg = sum/5
#     print(avg)

# avgof5(70,81,95,86,75)
# heros = ("thor", "kratos", "spiderman", "ironman", "gone")
# nums = (1, 2, 3, 5, 6, 7, 9)
# marks = [32,5,34,5,20,96]
# # def printlen(list):
#     print(len(list))

# printlen(heros)
# printlen(nums)
# printlen(marks)
# def printlist(list):
#     for i in list:
#         print(i, end = " ")
# printlist(heros)

# def converter(val):
#     print("usd =", val, "inr =",val*83)
# converter(70)    

# def show(n):              #recursive function
#     if(n == 0):
#         return
#     print(n)
#     show(n-1)
# show(8)
# def fact(n):
#     if(n == 1):                   #recursion se factorial
#         return 1
#     return fact(n-1)*n
# n = int(input("enter value:"))
# print(fact(n))
# def sum(n):
#     if(n == 0):
#         return 0              #sum of n no with recursion
#     return sum(n-1) + n

# n = int(input("enter value:"))
# print(sum(n))
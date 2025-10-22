# class student():
#     clg = "ramanu"
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#         print("adding")

# s1 = student("naveen",98,) 
# print(s1.name,s1.marks,s1.clg)                  
# s2 = student("kullu",95)
# print(s2.name,s2.marks,s1.clg)

# class student():
#     school = "ndes"
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks

#     def welcome(self):
#         print("welcome", self.name)    

# s1 = student("ganubai", "30",) 
# s2 = student("hero", 80)
# print(s1.name,s1.marks,s1.school) 
# s2.welcome()
# s1.welcome()      
 
# class student():
#     def __init__(self,name,mark):
#         self.name = name
#         self.mark = mark

#     def getavg(self):
#         sum = 0
#         for i in self.mark:
#             sum += i 
#         print(sum/3)       


   

# s1 = student("naveen",[81,95,70])     
# print(s1.name)
# s1.getavg()

# class car():                ####abstraction
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False
#     def startcar(self):
#         self.clutch = True
#         self.acc = True
#         print("car started.....")

# car1 = car()
# car1.startcar()      


# class account():
#     def __init__(self,accno,bal):
#         self.accno = accno
#         self.bal = bal

#     def credit(self,amount):
#        self.bal += amount
#        print(amount,"rupes credited")
#        print("total bal :",self.bal)

#     def debit(self,amount):
#         self.bal -= amount 
#         print(amount,"rupes debited")
#         print("total bal: ",self.bal)  

# per1 = account(1234567890,12000)        
# per1.credit(900)
# per1.credit(1000)
# per1.debit(590)
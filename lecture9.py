# class person:
#     __name = "dfdfvd"

#     def __hello(self):
#         print("hello mf")

#     def welcome(self):
#         print("welcomr")
#         self.__hello()
        

# p1 = person()
# p1.welcome()

class start():
    def __init__(self,type):
        self.type = type
    @staticmethod
    def st():
        print("car started")

    @staticmethod    
    def stop():
        print("car stoped")

class car(start):
    def __init__(self,name,type):
        self.name = name
        super().__init__(type)


c1 = car("supra","911")
print(c1.type)  
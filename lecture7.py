# file = open("sample.txt", "r")
# data = file.read()
# print(data)
# file.close
# f = open("sample.txt")
# a = f.readline()
# print(a)
# b = f.readline()
# print(b)
# f = open("demo.txt","w")
# f.write("randi ka bacha randy ortan\n")
# f.write("andi ki vha")
# f.close
# f = open("demo.txt", "a")
# f.write("\ngandu gyanai")
# data = f.read
# f.close
# f = open("demo.txt")
# data = f.read()
# print(data)
# with open("sample.txt","r") as f:
#     data = f.read()
#     print(data)

# with open("demo.txt","a+") as f:
#     f.write(" \nfuck u")
# import os
# os.remove("demo.txt")
# with open("practice.txt","r") as f:
#     data = f.read()

# newdata = data.replace("java", "python")
# with open("practice.txt", "w") as f:
#     f.write(newdata)
# word = input("search word: ")
# with open("practice.txt","r") as f:           search word
#     data = f.read()
#     if(data.find(word) != -1):
#         print("found")
#     else:
#         print("not found")   
def search_word(word):
     with open("practice.txt","r") as f:
        data = f.read          
        if(data.find(word) != -1):
            print("found")
        else:
            print("not found") 

search_word("we")
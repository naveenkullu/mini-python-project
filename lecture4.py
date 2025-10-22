dict = {
    "name" : "naveen",
    "surname" : "kullu",
    "age" : 19,
    "subject" : {
        "phy" : 70,
        "chem" : 95,
        "maths" : 81
    }
   
}
# print(dict.keys()) #sari key return karega
# print(len(dict))  #length print hogi no of keys
# print(dict.values())  #sirf values return ki karega baad wali value nhi araha toh karke dekh le
# print(list(dict.values()))    #list ke form me print hogi, aisa hum sabme kar skte h
# print(dict.items()) #tuple ki form me pair me values return krega
# pair = list(dict.items())
# print(pair[1]) agar koi specific key acces karta h ho to

# new_dict = { 
#     "name" : "jhantu",
#     "city" : "delhi",
#     "clg" : "ramanujan"
# }
# dict.update(new_dict)
# print(dict)   #dict mutable hoti h toh hum kuch bhi add karste h aur hum porana key change bhi kr skte h
# set = {1, 2, 2, 3 ,4, 5}
# set.add(0)
# set.remove(4)
# print(set)
# set2 = {"sec", "name", "ding", "2", "5", "9"}
# print(set2.pop()) #koi bhi random vlaue rerturn karega
# print(set.union(set2)) #se1 aur set2 ki sari valye print hogi bus koi bhi same value 2 bar nhi ayegi
# print(set.intersection(set2)) #kuch nhi comman nhi h isliye empty set ayega
#questions
# set1 = {"python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"}
# print(len(set1))
# mydict = {}
# a = int(input("phy:"))
# mydict.update({"phy" : a})
# b = int(input("chem:"))
# mydict.update({"chem" : b})
# c = int(input("maths:"))
# mydict.update({"maths" : c})
# print(mydict)
# set1 = {9, "9.0"}
# print(set1)

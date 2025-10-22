menu = {
    "pasta" : 120,
    "coffe" : 80,
    "momos" : 160,
    "dosa" : 40,
    "water" : 30,
    "samosa" : 34
}  

print("welcome here is menu")
print("pasta = Rs120\n"
"coffe = Rs80\n"
"momos = Rs160\n"
"dosa= Rs40\n"
"water= Rs30\n"
"samosa= Rs34")
bill = 0
item1 = (input("what do want to order= "))
if item1 in menu:
   a = (input("anything else? (yes/no) :"))
   if a == "yes":
      item2 = (input("what ? : "))
      bill += menu[item1]
      bill += menu[item2]
      print("here is bill =",bill)
   elif a == "no":
      print("fine")
      print("here is bill ")
      bill += menu[item1]
      print(bill)
   else:
      print("invailed try again")  
else:
   print("sorry we dont have this\nplease oreder somthing else")       
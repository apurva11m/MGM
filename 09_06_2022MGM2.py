#lists = changeable, ordered, allows duplication, indexed
mylist = ["Mumbai", "Chennai", "Delhi"]
#              #0         1          2
# print(mylist)

# print(len(mylist))

# print(type(mylist))

# print(mylist[1])

# mylist.append("Rajasthan")

# mylist.insert(2,"Assam")

list2 = ["Kerala","MP"]
mylist.extend(list2)

print(mylist)












#Tuple = ordered, unchangeable, allows duplication
# newtup = ("Mumbai", "Chennai", "Delhi")
# # newtup[2]="agra"
# print(newtup)

# mytup = ("Mumbai",)

# newtup = tuple(("Mumbai", "Chennai", "Delhi",24, 50.60, True, False))
#                  0          1         2     3     4     5      6
# print(len(newtup))

# print(type(newtup))
# print(type(mytup))

# print(newtup[1])

# print(newtup[1:3])
# print(newtup[2:])
# print(newtup[:6])

# newtup = ("Mumbai", "Chennai", "Delhi")
# x = list(newtup)
# # x[2]= "Agra"
# x.append("Haryana")
# x.remove("Chennai")
# newtup = tuple(x)
# print(newtup)

# newtup = ("Mumbai", "Chennai", "Delhi")
# for x in newtup:
#     print(x)

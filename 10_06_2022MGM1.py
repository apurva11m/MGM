#Dictionary - Ordered, changeable, Duplication not allowed
#key:value
# newdictinry= {
#     "Name":"Mike",
#     "Age":23,
#     "City":"Mumbai",
#     "Age":25,
#     "Result":True
# }

# dictinry1 = newdictinry.copy()
# print(dictinry1)

# print(newdictinry)

# print(len(newdictinry))

# print(newdictinry["City"])

# print(type(newdictinry))

# newdictinry["RollNo"] = 12

# newdictinry.update({"DOB":"12/6/2002"})
# print(newdictinry)

# newdictinry.pop("Result")

# newdictinry.popitem()

# del newdictinry

# del newdictinry["Name"]

# newdictinry.clear()

# print(newdictinry)

# students ={
#     "std1":{
#     "Name":"Mike",
#     "Age":23,
#     "City":"Mumbai",
#     "Result":True   
#     },

#     "std2":{
#     "Name":"John",
#     "Age":23,
#     "City":"Mumbai",
#     "Result":True

#     },

#     "std3":{
#     "Name":"Harry",
#     "Age":23,
#     "City":"Mumbai",
#     "Result":True
# }
# }

# print(students)

#Opewrators
#Arithmetic Operators
# x = 10
# y = 6
# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)
# print(x%y) #Modulus - returns the remainder
# print(x**y) #Exponent

#Assignment Operators
# x = 10
# x += 5  #x =x +5 = 10+5
# x -= 5  #x = 10-5
# x *= 5  #x = 10*5
# x /= 5  #x = 10/5
# x %= 5   #x = 10%5
# print(x)

# #Comparison Operators
# x =10
# y = 6
# print(x>y)
# print(x<y)
# print(x>=y)
# print(x<=y)
# print(x==y)
# print(x!=y)

# #Logical Operators
# x = 10
# y = 6
# print(x>y and x<y)
# print(x>y or x<y)
# print(not(x>y and x<y))

# #Identity Operators
# x = "Hello World"
# y = "Hello World"
# print(x is y)
# print(x is not y)

#Membership Operators
newtup = ("Mumbai", "Chennai", "Delhi")
print("Mumbai" in newtup)

print("Mumbai" not in newtup)
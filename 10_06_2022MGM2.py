# a = "H e l l o   W o r l d"
# #    0 1 2 3 4 5 6 7 8 9 10
#    -11-10-9-8-7-6-5-4-3-2-1 
# a = "Hello World"
# print(a)

#Slicing
# print(a[1:7])

# print(a[6:])

# print(a[:4])

# print(a[-4:-1])


# a = "      Hello world"
# print(a)
# # print(a.upper())
# # print(a.lower())

# print(a.strip())

# print(a.replace("o","l"))

# a = "Hello"
# # b = "Everyone"
# b = 20
# x = a+" " +b
# print(x)

# rollno = 26
# a = f"Roll no of Mike is {rollno}"
# a = "Roll no of Mike is"+ rollno
# print(a)

# a = "Roll no of Mike is {}"
# print(a.format(rollno))

# x = "Python is a high-level, interpreted, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming."
# print(x)

# y = '''Python is a high-level, interpreted, 
#                     general-purpose programming language. 
# Its design philosophy emphasizes code readability with the 
# use of significant indentation.

# Python is dynamically-typed and garbage-collected. 
# It supports multiple programming paradigms, including structured (particularly procedural), 
# object-oriented and functional programming.'''

# print(y)




#lists = changeable, ordered, allows duplication, indexed
mylist = ["Mumbai", "Chennai", "Delhi"]
#              #0         1          2
# print(mylist)

# print(len(mylist))

# print(type(mylist))

# print(mylist[1])

# mylist.append("Rajasthan")

# mylist.insert(2,"Assam")

# list2 = ["Kerala","MP"]
# mylist.extend(list2)

# print(mylist)

# mylist.remove("Mumbai")

# mylist.pop()
# mylist.pop(1)

# del mylist
# del mylist[2]

# mylist.clear()

# print(mylist)

# mylist.sort()

mylist.sort(reverse=True)
print(mylist)
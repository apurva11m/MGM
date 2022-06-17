#Function - block of code
#Built- in, User-defined
#performs logical, evaluative and computational tasks.

'''Syntax
#define a function
def func_name():
    logic/statement
    return output/expression
    
#calling a function
func_name()
'''

# def new_func():
#     print("Hello World")

# new_func()

#Passing Arguments
# def new_func(name):
#     print("Hello, "+name)

# new_func("Mike")

# def new_func(name1,name2):
#     print("Hello, "+name1+" and " +name2)

# new_func("Mike","John")

#Arbitrary arguments
def new_func(*name):
    print("Hello, "+name[2])

new_func("Mike","Ram","John","Harry","Sita")

# #Pass by value 
# name = "Mike"
# def new_func(name):
#     name = "John"
#     print("Hello, "+name)

# new_func(name)
# print("Outside the scope",name)


# #pass by reference
# def add_func(list):
#     list.append(20)
#     print("values", list)

# new_list = [50,80,40,6,0]
# add_func(new_list)
# print("the list", new_list)

#Keyword arguments
# def new_func(name1,name2):
#     print("Hello, "+name1+" and " +name2)

# new_func(name2 = "John",name1 = "Mike")

#Default value
# def new_func(name = "Shyam"):
#     print("Hello, "+name)

# new_func("Mike")
# new_func()

#Return Values
# def new_func(x):
#     return 2*x

# print(new_func(5))

# #Examples
# def square_num(n):
#     return n**2

# print(square_num(5))

''' Define a function that accepts radius and returns the area of a circle.'''
# # area = 3.14*r(square)
# radius= int(input("Enter the radius : "))
# def area(r) :
#     area = 3.14*(r**2)
#     return(area)

# print(area(radius))

# def areaofcircle(r):
#     a=3.14*r*r
#     print("Area of circle is :",a)

# areaofcircle(4)

'''Define a function that accepts roll number 
and returns whether the student is present or absent.'''
# present=[1,2,3,4,8,9,10,12]
# def fn(roll):
#     if roll in range(1,13):
#         if roll in present:
#             print(f"{roll} is present")
#         else:
#             print(f"{roll} is absent")
#     else:
#         print("Please enter a valid roll no ")
        
# roll=int(input("Enter a Roll No. between 1 to 12 : "))
# fn(roll)

# def attendence(roll):
#     x=[5,10,2,3,4,6,23]
#     if roll in x:
#         print(f"Roll number {roll} is present")
#     else:
#         print(f"Roll number {roll} is absent")

# roll=int(input("Enter the Roll No:"))
# attendence(roll)

# def rollno(n,r):
#     for i in range(len(n)):
#         if r in n:
#             print("Student is present.")
#             break
#         else:
#             print("Student is absent")
#             break
        
        

# n=int(input("Enter range of students roll no:"))
# n=[2,3,4,5,6,7,8]
# r=int(input("Enter your roll no:"))
# rollno(n,r)

# def fact(n):
#     pass



#Recursion
# from math import factorial


# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     return n* fact(n-1)

# a = fact(5)
# print(a)

# '''5=5*4*3*2*1
# 5 = 5*fact(4) = 4*fact(3) = 3*fact(2) = 2*fact(1) =1'''

def new_func(names):
    for x in names:
        print(x)

names = ["Mike","Ram","John","Harry","Sita"]

new_func(names)
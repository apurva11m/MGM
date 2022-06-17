#Loops
#1. if loop
#2. if elif loop
#3. if elif else loop

'''
if condition: (if this condition not satisfied control will move to the elif)
    statements to be executed if the"if" condition is satisfied
elif condition:(if this condition not satisfied control will move to the else)
    statements to be executed if the "elif" condition is satisfied
else: 
    if any of the condition is not satisfied it will by default get executed'''


# x = 10
# y = 5
# if x < y:
#     print("x is greater than y")
# elif x == y:
#     print("y is greater than x")
# else:
#     print("Both are equal")


# print("what is your age?")
# a = input()
# print("My name is " +a)

# print("enter no.1")
# a = int(input())
# print("enter no2")
# b = int(input())
# c = a+b
# print(f"sum is {c} ")



'''Write a program to
check whether a person is eligible for voting or not. 
(accept age from user)'''

print("Enter your age:")
age = (int(input()))
if age>=18 :
    print("you are eligible for voting")
else:
    print("you are not eligible for voting")

# print("Enter youe age")
# a = int(input())
# if a < 18:
#     print("you r not eligible for voting")
# else:
#     print("you r eligible for voting")




'''Write a program to check whether a number is divisible by 5 or not.'''
# print("Enter a number:")
# num = int(input())
# if num%5==0:
#     print("Number is divisible by 5")
# else:
#     print("Number is not divisible by 5")


# x=int(input("Enter a number: "))

# if x%5==0:
#     print("%d is divisible by 5"%x)

# else:
#      print("%d is not divisible by 5"%x)

# x = 10
# y = 5
# # if x>y: print("x is greater than y")

# print("x is greater") if x < y else print("y is greater")

# if x>y:
# #     pass

# x = 100

# if x >50 or x >175:
#     print("x is greater than 50")
#     if x>25:
#         print("x is greater than 25")
#     else:
#         print("not greater than 25")
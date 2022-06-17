'''Find the factorial of a given number
Write a program to use the loop to find the factorial of a given number.

The factorial (symbol: !) means to multiply all whole numbers from the chosen number
down to 1.

For example: calculate the factorial of 5

5! = 5 × 4 × 3 × 2 × 1 = 120
Expected output:

120'''

# number = int(input("Enter a no : "))
# num= number
# fact = 1
# while(number>0):
#     fact = fact*number
#     number-=1
# print(f"{num}! is {fact}")


# num = int(input("Enter a number: ")) 
# factorial = 1 
# if num < 0: 
#    print(" Factorial does not exist for negative numbers") 
# elif num == 0: 
#    print("The factorial of 0 is 1")    
# else:  
#    for i in range(1,num + 1):    
#       factorial = factorial*i    
#    print("The factorial of",num,"is",factorial)














'''Write a Python program that accepts a string and calculate the number of digits and 
letters. 
a.isalpha(), a.isdigit()
Sample Data : Python 3.2
Expected Output :
Letters 6
Digits 2''' 

# data= "python 3.2"
# k=0
# letter=0
# digit=0
# for k in range(0,len(data)) :
#     if data[k].isalpha():
#         letter+=1
#     elif data[k].isdigit():
#         digit+=1
# print(f"Letters {letter}")
# print(f"Digits {digit}")


# txt="Python 3.2"
# strCount=0
# digitCount=0
# for i in txt:
#     if i.isalpha():
#         strCount=strCount+1
#     elif i.isdigit():
#         digitCount=digitCount+1
#     else:
#         pass

# print("alphabet count:",strCount)
# print("digit Count:",digitCount)

# a = input("Enter a string: ")

# alpha = 0
# digit = 0
# for i in range(0,len(a)):
#     if a[i].isalpha():
#      alpha+=1
#     elif a[i].isdigit():
#         digit+=1

# print(f'letters: {alpha}')
# print(f'digits: {digit}')
















'''Use a loop to display elements from a given list present at odd index positions
Given:

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Note: list index always starts at 0

Expected output:

20 40 60 80 100'''

# my_lst=[10,20,30,40,50,60,70,80,90,100]
# for i in range(len(my_lst)):
#     if(i%2!=0):
#         print(my_lst[i], end=" ")


# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# for i in my_list[1::2]:
#      print(i, end=" ")















'''Display numbers from -10 to -1 using for loop
Expected output:

-10
-9
-8
-7
-6
-5
-4
-3
-2
-1'''

# for i in range(-10,0):
#     print(i)

# i=-10
# while(i<=-1):
#     print(i)
#     i+=1
















'''WAP to separate positive and negative number from a list.
Hint 1 
Given x = [23, 4, -6, 23, -9, 21, 3, -45, -8]

Expected output 
Result:
Positive: [23, 4, 23, 21, 3] Negative: [-6, -45, -9, -8]'''

















'''Write a Python program that accepts a word from the user and reverse it.'''
txt=input("Enter a Word that you want to reverse: ")
print(txt[::-1])























'''Write a program that appends the type of elements from a list.
Hint 1 
Given x = [23, ‘Python’, 23.98]

Expected output 
Result:
[<class ‘int’>,<class ‘str’>,<class ‘float’>]'''


my_list =[23,"python",23.98]
for i in range(0,len(my_list)):
     print(my_list[i],type(my_list[i]),end= "")

# lst=[22,'I am a string',33.4]
# new_lst=[]
# for x in lst:
#     val=type(x)
#     new_lst.append(val)
# print(new_lst)

# list = [23,'python', 23.98]
# for item in list :
#     print(type(item), end=" ")

#For loop
# cities = ["Mumbai", "Chennai", "Delhi"]
# for x in cities:
#     print(x)

# for x in "Mumbai":
#     print(x)

# cities = ["Mumbai", "Chennai", "Delhi"]
# for x in cities:
#     print(x)
#     if x == "Chennai":
#         break

# cities = ["Mumbai", "Chennai", "Delhi"]
# for x in cities:
#     if x == "Chennai":
#         break
#     print(x)

# cities = ["Mumbai", "Chennai", "Delhi"]
# for x in cities: 
#     if x == "Chennai":
#         continue
#     print(x)
    

# cities = ["Mumbai", "Chennai", "Delhi"]
# for x in cities:
#     print(x)
# else:
#     print("List is over.")


# cities = ["Mumbai", "Chennai", "Delhi"]
# countries = ["India", "US","UK"]
# for x in cities:
#     for y in countries:
#         print(x,y)

# for x in range(5): #(0,5,1)
#     print(x)

# for x in range(2,5): #(2,5,1)
#     print(x)

# for x in range(1,5,2):
#     print(x)

'''Display Fibonacci series up to 10 terms
The Fibonacci Sequence is a series of numbers. 
The next number is found by adding up the two numbers before it. 
The first two numbers are 0 and 1.

For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. 
The next number in this series above is 13+21 = 34.'''

'''0, 1, 1, 2, 3, 5, 8, 13, 21
0,1,
n1 = 0, n2 =1
sum = n1+n2 = 0+1 =1
0,1,1
n1 = 1, n2 =1
sum = n1+n2 =1+1=2
# 0,1,1,2'''

# n1 , n2 = 0 , 1
# print("Fibonacci series:")
# for i in range(10):
#     print(n1,end =" ") 
#     sum = n1 +n2
#     n1 = n2
#     n2 = sum


'''Write a Python program to count the number of even and odd numbers from a series of 
numbers. 
	Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
	Expected Output :
	Number of even numbers : 4
	Number of odd numbers : 5
	
'''
list1=[1,2,3,4,5,6,7,8,0,9]
even=0
odd=0
for i in list1:
    if i%2==0:
        even+=1
    else:
        odd+=1

print(f'There are {even} Even and {odd} Odd numbers')

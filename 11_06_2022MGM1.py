'''Accept three sides of triangle and check whether the triangle is possible or not.
(triangle is possible only when sum of any two sides is greater than 3rd side)'''

# a= int(input("Enter a  1st side: "))
# b= int(input("Enter a  2nd side: "))
# c= int(input("Enter a  3rd side: "))

# if a+b>c and b+c>a and a+c>b :
#     print("triangle is possible")
# else:
#     print("triangle is not possible")


'''Write a program to calculate the electricity bill (accept number of unit from user) 
according to the following criteria :
    Unit                                                         Price  
First 100 units                                               no charge amt = 0
Next 100 units   {unit>100 unit<=200}                         Rs 5 per unit
After 200 units                                               Rs 10 per unit

95 ---->0
100 --->0
101 ---> 5
150 ---> (150-100)5      {100 - 200}
201 ---> 10(201-200)     {200>}
# (For example if input unit is 350 than total bill amount is 1500)
# '''
# unit = int(input("Enter no of units: "))

# if unit<=100 :
#     print("Total bill amount is 0")
# elif  unit<=200:
#     amount = (unit-100)*5
#     print(f"Total bill amount is {amount}")
# else :
#     amount = (100*5)+(unit-200)*10
#     print(f"Total bill amount is {amount}")

'''
450
100=0
100=100*5=500
250=250*10=2500
total bill =3000'''


#While Loop
#while condition:
#     stmt executed until the condition is true
# i = 1
# while i <10:
#     print(i)
#     i += 1 #i=i+1

# Break
i = 1
while i <10:
    print(i)
    if i==5:
        break
    i += 1 #i=i+1

# #Continue
# i = 1
# while i <10:
#     i += 1
#     if i==5:
#         continue
#     print(i)
     

# i = 1
# while i <10:
#     print(i)
#     i += 1 #i=i+1
# else:
#     print("i is greater than 10")

# i= 1
# while i <10:
#   print(i)
#   if i ==5:
#     break
# i +=1


'''Write a program to print the following using while loop
First 10 Even,Odd,Natural numbers'''
print("****The First 10 Even Numbers****")
i = 1
while(i <= 10):
    print(2 * i)
    i = i + 1

print("****The First 10 Odd Numbers****")
i = 1
while(i <= 10):
 print(2 * i - 1)
 i = i + 1

print("****The First 10 Natural Numbers****")
i = 1
while(i <= 10):
   print(i)
   i = i + 1


#even no.s
print("First 10 even no.s")
i = 0
while i<20:
    print(i)
    i +=2

#odd no.s
print("First 10 odd no.s")
i = 1
while i<20:
    print(i)
    i+=2

i=1
print("first 10 Natural numbers")
while(i<=10) :
    print(i)
    i+=1
else:
    i=1
j=1
print("first 10 even numbers")
while(i<=10) :
    if(j%2==0):
        print(j)
        i+=1
    j+=1
else:
    i=1
    j=1
print("first 10 odd numbers")
while(i<=10) :
    if(j%2!=0):
        print(j)
        i+=1
    j+=1

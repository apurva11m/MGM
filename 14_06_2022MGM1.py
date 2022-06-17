#Inheritance
#Single Inheritance
'''
class base_class:
    statements

class derived(base_class):
    statements
'''

# class Vehicle:
#     def fuel(self):
#         print("The fuel is required")

# class Car(Vehicle):
#     def fuel_type(self):
#         print("Type of fuel required is petrol")

# c1 = Car()
# c1.fuel()
# c1.fuel_type()

#Multiple Inheritance
'''
class base_class1:
    statements

class base_class2:
    statements

class base_class3:
    statements

class derived(base_class1, base_class2, base_class3):
    statements
'''

# class Vehicle:
#     def fuel(self):
#         print("The fuel is required")

# class Machine:
#     def engine(self):
#         print("Engine used is xyz")

# class Car(Vehicle,Machine):
#     def fuel_type(self):
#         print("Type of fuel required is petrol")

# c1 = Car()
# c1.fuel()
# c1.fuel_type()
# c1.engine()


#Multilevel Inheritance
'''
class base_class1:
    statements

class base_class2(base_class1):
    statements

class base_class3(base_class2):
    statements

# '''

# class Vehicle:
#     def fuel(self):
#         print("The fuel is required")

# class Car(Vehicle):
#     def fuel_type(self):
#         print("Type of fuel required is petrol")

# class Honda(Car):
#     def seats(self):
#         print("5 seats are there.")

# h1 = Honda()
# h1.fuel()
# h1.fuel_type()
# h1.seats()


#Hierarchical Inheritance
'''class base_class1:
    statements

class class1(base_class1):
    statements

class class2(base_class1):
    statements

class class3(base_class1):
    statements


'''

# class Vehicle:
#     def fuel(self):
#         print("The fuel is required")

# class Car(Vehicle):
#     def fuel_type(self):
#         print("Type of fuel required is petrol")

# class Truck(Vehicle):
#     def mileage(self):
#         print("Type of fuel required is petrol")

# class Bus(Vehicle):
#     def tyre(self):
#         print("Type of fuel required is petrol")

# c1 = Car()
# c1.fuel()
# c1.fuel_type()
# t1 = Truck()
# t1.fuel()
# t1.mileage()
# b1 = Bus()
# b1.fuel()
# b1.tyre()

# #Hybrid
'''class base_class1:
    statements

class class1(base_class1):
    statements

class class2():
    statements

class class3(class1,class2):
    statements
'''

# class Vehicle:
#     def fuel(self):
#         print("The fuel is required")

# class Car(Vehicle):
#     def fuel_type(self):
#         print("Type of fuel required is petrol")

# class Honda():
#     def seats(self):
#         print("5 seats are there.")

# class xyz_variant(Car, Honda):
#     def colour(self):
#         print("Type of fuel required is petrol")

'''Write a Python program to create a Vehicle class with max_speed and mileage instance
 attributes.'''
# class Vehicle:
#     def __init__(self,max_speed,mileage):
#         self.max_speed=max_speed
#         self.mileage=mileage
#     def display(self):
#         print(f"Max speed of the Vehicle is {self.max_speed} and its Mileage is {self.mileage}")
# obj=Vehicle("90kmph","50")
# obj.display()


class Vehicle:
    def max_speed(self):
        print("The max_speed is 100m/s")

class Car(Vehicle):
    def mileage(self):
        print("The mileage is required")

c1 = Car()
c1.max_speed()
c1.mileage()


# class Vehicle:
#     def __init__(self, max_speed, mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage
        
        
# car = Vehicle(220, 10000)
# print(car.max_speed, car.mileage)

# class Vehicle:
#     def max_speed(self):
#         print("The max_speed is 100m/s")
#     def mileage(self):
#         print("The mileage is required")

# class Car(Vehicle):
#     pass

# c1 = Car()
# c1.max_speed()
# c1.mileage()

#Polymorphism
#Encapsulation

'''Create a Python class called BankAccount which represents a bank account, having as 
attributes: accountNumber (numeric type), name (name of the account owner as string type),
 balance.
Create a constructor with parameters: accountNumber, name, balance.
Create a Deposit() method which manages the deposit actions.
Create a Withdrawal() method  which manages withdrawals actions.
Create an bankFees() method to apply the bank fees with a percentage of 5% of the
balance account.
Create a display() method to display account details.
Give the complete code for the  BankAccount class.'''

# class BankAccount:
#     def __init__(self,accountNumber,name,balance):
#         self.accountNumber =accountNumber
#         self.name =name
#         self.balance = balance

#     def Deposit(self,d):
#         self.balance = self.balance +d

#     def Withdrawal(self,w):
#         if(self.balance<w):
#             print("Insufficient balance")
#         else:
#             self.balance = self.balance-w

#     def bankFees(self):
#         self.balance = 0.95*self.balance

#     def display(self):
#         print("Account Number:" , self.accountNumber)
#         print("Account Name:" , self.name)
#         print("Account Balance:" , self.balance)

# n1 = BankAccount(219878545, "Harry", 25000)
# n1.Withdrawal(5000)
# n1.Deposit(2000)
# n1.display()
# n1.bankFees()


# class Bank_acc:
#     def __init__(self,acc_num,name,balance):
#         self.acc_num=acc_num
#         self.name=name
#         self.balance=balance
#     def Deposit(self):
#         dep=int(input("Enter the amount you want to deposit: "))
#         new_bal=self.balance+dep
#         print(f"You have successfully deposited Rs.{dep} and your updated balance is {new_bal} ")
#     def Withdrawl(self):
#         draw=int(input("Enter the Amount you want to withdraw: "))
#         if draw<=self.balance:
#             self.balance=self.balance-draw
#             print(f"You have withdrawn Rs.{draw} and you updated balance is {self.balance}")
#         else:
#             print("Insufficient Balance")
#     def bankfees(self):
#         self.balance=(self.balance*5)/100
#         print(f"Bank fees : {self.balance}")
#     def display(self):
#         print("Your Account details: ")
#         print(f"Your Account number is {self.acc_num}")
#         print(f"Your Account Name is {self.name}")
#         print(f"Your Account Balance is {self.balance}")
# obj=Bank_acc(123456789,"Roshni Gupta",200000)
# obj.Deposit()
# obj.Withdrawl()
# obj.bankfees()
# obj.display()

#Stack
'''pop, push, is full, is empty, display'''
# class Stack:
#     def __init__(self,max_size):
#         self.__max_size=max_size
#         self.__elements=[None]*self.__max_size
#         self.__top=-1

#     def is_full(self):
#         if(self.__top==self.__max_size-1):
#             return True
#         return False

#     def is_empty(self):
#         if(self.__top==-1):
#             return True
#         return False

#     def push(self,data):
#         if(self.is_full()):
#             print("The stack is full!!")
#         else:
#             self.__top+=1
#             self.__elements[self.__top]=data

#     def pop(self):
#         if (self.is_empty()):
#             print("Stack is empty, Cant Pop...")
#         else:
#             data=self.__elements[self.__top]
#             self.__top-=1
#             return data

#     def get_max_size(self):
#         return self.__max_size

#     def display(self):
#         if(self.is_empty()):
#             print("The stack is empty")
#         else:
#             index=self.__top
#             while(index>=0):
#                 print(self.__elements[index])
#                 index-=1


# stack1=Stack(5)
# #Push all the required element(s).
# stack1.push("Shirt1")
# stack1.push("Shirt2")
# stack1.push("Shirt3")
# stack1.push("Shirt4")
# stack1.push("Shirt5")
# stack1.push("Shirt6")

# #Pop an element
# print(stack1.pop())
# stack1.display()

# #queue
class Queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0

    def is_full(self):
        if(self.__rear==self.__max_size-1):
                return True
        return False
    
    def is_empty(self):
        if(self.__front>self.__rear):
            return True
        else:
            return False

    def enqueue(self, data):
        if (self.is_full()):
            print("The Queue is full!!")
        else:
            self.__rear +=1
            self.__elements[self.__rear] = data

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty , Cant Dequeue")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data

    def display(self):
        for index in range(self.__front,self.__rear+1):
            print(self.__elements[index])

    def get_max_size(self):
         return self.__max_size

queue1=Queue(5)
#Enqueue all the required element(s).
queue1.enqueue("Tom")
queue1.enqueue("Dick")
queue1.enqueue("Harry")
queue1.enqueue("Jack")
queue1.enqueue("Maria")
#Dequeue all the required element(s).
data=queue1.dequeue()
#Display all the elements in the queue.
queue1.display()


# class Queue:
#     def __init__(self,max_size):
#         self.__max_size=max_size
#         self.__elements=[None]*self.__max_size
#         self.__front = 0
#         self.__rare =-1

#     def get__max_size(self):
#         return self.get__max_size

#     def is_full(self):
#         if(self.__rare==self.__max_size-1): 
#             return True
#         return False  

#     def enqueue(self,data):
#         if(self.is_full()):
#             print("Queue is full !!!")
#         else:
#             self.__rare+=1
#             self.__elements[self.__rare]=data         

#     def is_empty(self):
#         if(self.__front > self.__rare):
#             return True
#         return False

#     def dequeue(self):
#         if(self.is_empty()):
#             print("Queue is empty")  
#         else :
#             data=self.__elements[self.__rare]
#             self.__front+=1
#             return data


#     def display(self):
#         for index in range(self.__front,self.__rare+1):
#             print(self.__elements[index])

# queue1=Queue(5)
# queue1.enqueue("one")
# queue1.enqueue("Two") 
# queue1.enqueue("Three") 
# queue1.enqueue("Four") 
# queue1.enqueue("Five") 
# # queue1.enqueue("Six")  
# queue1.is_full()  
# queue1.display()

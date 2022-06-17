class Node:
    def __init__(self,data):
        self.data = data #data to be stored.
        self.next = None #address of the next node.
        self.prev = None #address of the previous node.

class double_link_list():
    def __init__(self):
        self.head = None

    def push(self,data): #adding node at the start
        n_node = Node(data)
        n_node.next = self.head #updating the nextaddress of new node as head.
        n_node.prev = None
        if self.head is not None: #checking is head is none or not.

            self.head.prev = n_node #updating the previous address of head(which was none before) to the new node 
        self.head = n_node #making the new node the head

    def insert(self, prev_node, data):
        if prev_node is None:# check is previous node is none or not
            return
        n_node = Node(data)
        n_node.next = prev_node.next#updating the next of the new node
        prev_node.next = n_node #updating the next of the previous node 
        n_node.prev = prev_node #updating the previous of the new node
        if n_node.next is not None:
            n_node.next.prev = n_node #updating the new node's next node's previous address.

    def append(self, data):
        n_node =Node(data)
        n_node.next = None #making the next of new node none.
        if self.head is None: #checking if head is none or not
            n_node.prev = None #if yes make the previous of the new node none
            self.head = n_node #make the new node the new head
            return
        last = self.head
        while(last.next is not None): #move till the last node
            last = last.next
        last.next = n_node #updating the address of new node in last node's next.
        n_node.prev = last #updating the address of last node in new node's previous.
        return

    def display(self, node):
        while(node is not None):  #printing in forward direction
            print(node.data)
            last = node
            node = node.next

        # while(last is not None): #printing in backward direction
        #     print(last.node)
        #     last = last.prev

    def delete(self, data):
        if self.head is None or data is None:
            return 

        if self.head == data: #if head is the node to be deleted
            self.head =data.next #make the next node the head

        if data.next is not None: #if there is next node present.
            data.next.prev = data.prev #connect it with the previous node

        if data.prev is not None: #if there is previous node present
            data.prev.next = data.next #connect it with the next node


d1 = double_link_list()
d1.push(2)
d1.push(3)
d1.push(4)
d1.display(d1.head)

#INFYTQ QUESTION
'''Given a stack of integers, write a python program that updates the input stack such that all occurrences of the smallest values are at the bottom of the stack, while the order of the other elements remains the same.

For example:
Input stack (top-bottom) :   5 66  5  8  7
Output:  66  8  7  5  5
 '''
class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__top=-1

    def is_full(self):
        if(self.__top==self.__max_size-1):
            return True
        return False

    def is_empty(self):
        if(self.__top==-1):
            return True
        return False

    def push(self,data):
        if(self.is_full()):
            print("The stack is full!!")
        else:
            self.__top+=1
            self.__elements[self.__top]=data

    def pop(self):
        if(self.is_empty()):
            print("The stack is empty!!")
        else:
            data= self.__elements[self.__top]
            self.__top-=1
            return data

    def display(self):
        if(self.is_empty()):
            print("The stack is empty")
        else:
            index=self.__top
            while(index>=0):
                print(self.__elements[index])
                index-=1

    def get_max_size(self):
        return self.__max_size

    #You can use the below __str__() to print the elements of the DS object while debugging
    # def __str__(self):
    #     msg=[]
    #     index=self.__top
    #     while(index>=0):
    #         msg.append((str)(self.__elements[index]))
    #         index-=1
    #     msg=" ".join(msg)
    #     msg="Stack data(Top to Bottom): "+msg
    #     return msg

def change_smallest_value(number_stack):
    l=[]
    while(not number_stack.is_empty()):
        l.append(number_stack.pop())
    mini = min(l)
    counter = l.count(min(l))
    for i in range(counter):
        number_stack.push(mini)
    for element in l[::-1]:
        if element!=mini:
            number_stack.push(element)
    return number_stack 
#Add different values to the stack and test your program
number_stack=Stack(8)
number_stack.push(90)
number_stack.push(3)
number_stack.push(3)
number_stack.push(7)
number_stack.push(4)
print("Initial Stack:")
number_stack.display()
# change_smallest_value(number_stack)
print("After the change:")
number_stack.display()








        

        









    




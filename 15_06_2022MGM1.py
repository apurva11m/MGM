class Node:
    def __init__(self,data):
        self.__data=data #data stored inside the node
        self.__next=None #address/pointer to the next node
    
    def get_data(self):
        return self.__data
    
    def set_data(self,data):
        self.__data=data
    
    def get_next(self):
        return self.__next
    
    def set_next(self,next_node):
        self.__next=next_node

class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None
    
    def get_head(self):
        return self.__head
    
    def get_tail(self):
        return self.__tail
    
    def add(self,data):
        new_node = Node(data)
        if(self.head is None): #no node is present
            self.__head=self.__tail=new_node #when single node is present head tail both point to it.
        else:
            self.__tail.set_next(new_node) #adding the address of new node to the previous tail. 
            self.__tail = new_node #making the new node the new tail.

       
    def display(self):   
        temp = self.__head
        print("Data stored in linked list are :")

        while(temp != None):
            print(temp.get_data())
            temp = temp.get_next()

    
    def find_node(self,data):
        temp = self.__head
        print("Data stored in linked list are :")

        while(temp != None):#check whether nodes are present or not
            if(temp.get_data()==data): #compare the data of node to the passed value
                return temp
            temp = temp.get_next()#search for the next value
        return None
       
    def insert(self,data,data_before):
        new_node = Node(data)
        if(data_before == None):
            new_node.set_next(self.__head)#linking the address of head to the new node
            self.__head = new_node #making the new node the head
            if(new_node.get_next()==None): # checking if new node is the only node present
                self.__tail= new_node #if yes make it the tail 

        else:
            node_before=self.find_node(data_before)
            if(node_before is not None):
                new_node.set_next(node_before.get_next())#linking the address of next succeding node to the new node
                node_before.set_next(new_node) #linking the address of precceding node to the new node
                if(new_node.get_next() is None):#new node is the last node
                    self.__tail= new_node #make the new node the tail
            else:
                print(data_before,"is not present")

    def delete(self,data):
        node=self.find_node(data)
        if(node is not None):
            if(node==self.__head):
                if(self.__head==self.__tail):
                    self.__tail=None
                self.__head=node.get_next()
            else:
                temp=self.__head
                while(temp is not None):
                    if(temp.get_next()==node):
                        temp.set_next(node.get_next())
                        if(node==self.__tail):
                            self.__tail=temp
                        node.set_next(None)
                        break
                    temp=temp.get_next()
        else:
            print(data,"is not present in Linked list")



        
       

list1=LinkedList()
#Add all the required element(s)
#Insert the element in the required position
# list1.insert("NewItem","Sugar")
list1.delete("Sugar")
list1.display()
                   
# linked list deletion in python
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def push(self,newdata):
        newnode=Node(newdata)
        newnode.next=self.head
        self.head=newnode
    def deletenode(self,key):
        temp=self.head
        if temp is not None:
            if temp.data==key:
                self.head=temp.next
                temp=None
                return
        while temp is not None:
            if temp.data==key:
                break
            prev=temp
            temp=temp.next
        if temp==None:
            return
        prev.next=temp.next
        temp=None
    def printList(self):
        temp=self.head
        while temp:
            print(f"{temp.data}")
            temp=temp.next
llist=LinkedList()
# llist.push(7)
# llist.push(1)
# llist.push(3)

while True:
    choice=int(input("Enter your choice 1 for insertion 2 for deletion 3 to display 4 to exit"))
    if choice==1:
        data=int(input("Enter data to be inserted"))
        llist.push(data)
        continue
    elif choice==2:
        data=int(input("Enter data to be deleted"))
        llist.deletenode(data)
        continue
    elif choice==3:
        print("the created linked list is")
        
        llist.printList()
        continue
    else:
        break


        
# print("created linked list\n")
# llist.printList()
# # llist.deletenode(1)
# print("linked list after deletion\n")
# llist.printList()

    
    
    
    
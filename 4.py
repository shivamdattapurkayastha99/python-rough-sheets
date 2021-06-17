# circular linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class CircularLinkedList:
    def __init__(self):
        self.last=None
    def addToEmpty(self,data):
        if self.last!=None:
            return self.last
        temp=Node(data)
        self.last=temp
        self.last.next=self.last
        return self.last
    def addBegin(self,data):
        if self.last==None:
            return self.addToEmpty(data)
        temp=Node(data)
        temp.next=self.last.next
        self.last.next=temp
        return self.last
    def addEnd(self,data):
        if self.last==None:
            return self.addToEmpty(data)
        temp=Node(data)
        temp.next=self.last.next
        self.last.next=temp
        self.last=temp
        return self.last
    def addAfter(self,data,item):
        if self.last==None:
            return None
        temp=Node(data)
        p=self.last.next
        while p:
            if p.data==item:
                temp.next=p.next
                p.next=temp
                if p==self.last:
                    self.last=temp
                    return self.last
                else:
                    return self.last
            p=p.next
            if p==self.last.next:
                print(f"{item} not present in the list")
                break
    def traverse(self):
        if self.last==None:
            print("List is empty")
            return
        temp=self.last.next
        while temp:
            print(f"{temp.data} ")
            temp=temp.next
            if temp==self.last.next:
                break
if __name__ == "__main__":
    llist=CircularLinkedList()
    
    
    while True:
        ch=int(input("Enter the choice 1 for add to empty 2 for add to begin 3 for add to end 4 for add after 5 to break"))
        if ch==1:
            data=int(input("Enter the data to be inserted in empty list"))
            last=llist.addToEmpty(data)
        elif ch==2:
            data=int(input("Enter the data to be inserted at the begin"))
            last=llist.addBegin(data)
        elif ch==3:
            data=int(input("Enter the data to be inserted at the end"))
            last=llist.addEnd(data)
        elif ch==4:
            item=int(input("Enter the item after which data is to be inserted "))
            data=int(input("Enter the data to be inserted at after item"))
            last=llist.addAfter(data,item)
        else:
            llist.traverse()
            break
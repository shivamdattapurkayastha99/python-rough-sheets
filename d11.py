# to reverse a linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def reverseUtil(self,curr,prev):
        if curr.next is None:
            self.head=curr
            curr.next=prev
            return
        next=curr.next
        curr.next=prev
        self.reverseUtil(next,curr)
    def reverse(self):
        if self.head is None:
            return
        self.reverseUtil(self.head,None)
    def push(self,newdata):
        newnode=Node(newdata)
        newnode.next=self.head
        self.head=newnode
    def printlist(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
ll=linkedlist()
ll.push(8)
ll.push(7)
ll.push(6)
ll.printlist()
ll.reverse()
print("reverse linked list")
ll.printlist()

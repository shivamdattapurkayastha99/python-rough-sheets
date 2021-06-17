# queue using stack
class Queue:
    def __init__(self):
        self.s1=[]
        self.s2=[]
    def enqueue(self,x):
        while len(self.s1)!=0:#first stack
            self.s2.append(self.s1[-1])
            self.s1.pop()
        self.s1.append(x)
        while len(self.s2)!=0:#second stack
            self.s1.append(self.s2[-1])
            self.s2.pop()
    def dequeue(self):
        if len(self.s1)==0:
            print("Queue is empty")
        x=self.s1[-1]
        self.s1.pop()
        return x
if __name__ == "__main__":
    q=Queue()
    n=int(input("Enter the no of elements you enter in the stack"))
    for i in range(n):
        data=int(input("Enter the data you want to insert the stack"))
        q.enqueue(data)
    for i in range(n):
        
        print(q.dequeue())

            
            

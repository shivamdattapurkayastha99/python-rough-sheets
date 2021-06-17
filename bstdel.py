# python program to perform binary search tree deletion

class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
def inorder(root):
        if root is not None:
            inorder(root.left)
            print(root.key,end=" ")
            inorder(root.right)
def insert(node,key):
        if node is None:
            return Node(key)
        if key<node.key:
            node.left=insert(node.left,key)
        else:
            node.right=insert(node.right,key)
        return node
def minValueNode(node):
        current=node
        while(current.left is not None):
            current=current.left
        return current
def deletenode(root,key):
        if root is None:
            return root
        if key<root.key:
            root.left=deletenode(root.left,key)
        elif key>root.key:
            root.right=deletenode(root.right,key)  
        else:
            if root.left is None:
                temp=root.right
                root=None
                return temp
            elif root.right is None:
                temp=root.left
                root=None
                return temp
            temp=minValueNode(root.right)
            root.key=temp.key
            root.right=deletenode(root.right,temp.key)
        return root
root=None

while True:
    
    ch=int(input("Enter your choice 1.for insertion,2.for deletion,3.to display inorder,4.to exit"))
    if ch==1:
        data=int(input("Enter the data to be inserted"))
        root=insert(root,data)
        continue
    if ch==2:
        data=int(input("Enter the data to be deleted"))
        root=deletenode(root,data)
        continue
    if ch==3:
        
        print(inorder(root))
        continue
        
    else:
        break

        





from Queue import Queue
from Stack import Stack
class Node:
    def __init__(self,val=None,left=None,right=None):
        self.val = val
        self.left = left
        self.right=right
    def __repr__(self):
        return f" {self.val}"


class BST:
    def __init__(self, root=None):
        self.root = root
    
    def addNode(self,val):
        newNode = Node(val)
        if not self.root: 
            self.root = newNode
            return

        current = self.root
        parent = None

        while current:

            parent = current
           
            if val <= current.val:
                current = current.left
                if current == None:
                    parent.left = newNode
                    return
            else:
                current = current.right
                if current == None:
                    parent.right = newNode
                    return
            
    def preorderTraversal(self,node):
        if node == None:
            return

        print(node.val)
        self.preorderTraversal(node.left)
        self.preorderTraversal(node.right)
    def postorderTraversal(self,node):
        if node == None:
            return
    
        self.postorderTraversal(node.left)
        self.postorderTraversal(node.right)

        print(node.val)
    def inorderTraversal(self,node): 
        if node == None:
            return
    
        self.inorderTraversal(node.left)
        print(node.val)
        self.inorderTraversal(node.right)

    def levelorderTraversal(self):
        queue = Queue()
        queue.enqueue(self.root)

        while not queue.isEmpty():
            current = queue.dequeue()
            print(current.val)

            if current.left:
                queue.enqueue(current.left)
            
            if current.right:
                queue.enqueue(current.right)
    
    def stackPreorderTraversal(self):
        stack = Stack()
        stack.push(self.root)

        while not stack.isEmpty():
            current = stack.pop()
            print(current.val)

            if current.right: 
                stack.push(current.right)
            if current.left:
                stack.push(current.left)

            
        
        
        


            
            



root = Node(4)

bst = BST(root)

bst.addNode(2)
bst.addNode(1)
bst.addNode(6)
bst.addNode(5)
bst.addNode(3)
bst.addNode(7)

# bst.preorderTraversal(root)
# bst.postorderTraversal(root)
# bst.inorderTraversal(root)
bst.levelorderTraversal()
# bst.stackPreorderTraversal()






    
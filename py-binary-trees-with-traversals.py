import constants as Site
DZ = Site.Core()
DZ.line("DZ module initiated")
#import inspect
import pprint
__pp = pprint.PrettyPrinter(indent=4)
######################### HEADER ##########################

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
        
    def find(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval) + " is not Found"
            return self.left.find(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval) + " is not Found"
            return self.right.find(lkpval)
        else:
            return str(self.data) + " is found"
    
    # in-order traversal
    def inOrderTraversal(self, root):
        pass
    
    # pre-order traversal
    def preOrderTraversal(self, root):
        pass
    
    # post-order traversal
    def postOrderTraversal(self, root):
        pass
    
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()
    
root = Node(12)
root.insert(6)
root.insert(3)
root.insert(14)
root.insert(35)
root.insert(31)
root.insert(10)
root.insert(19)

print(root.find(7))
print(root.find(19))

root.PrintTree()
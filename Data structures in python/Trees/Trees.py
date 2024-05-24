class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def Inorder(root): # Do Leetcode Problems 
    if root == None:
        return
    Inorder(root.left)
    print(root.data,end = ' ')
    Inorder(root.right)
def Preorder(root):
    if root == None:
        return
    print(root.data,end=' ')
    Preorder(root.left)
    Preorder(root.right)
def Postorder(root):
    if root == None:
        return
    Postorder(root.left)
    Postorder(root.right)
    print(root.data,end = ' ')
def LevelOrder(root):
    # q=[]
    if root == None:
        return
    result = []
    q = [root]
    while len(q) != 0 :
        subresult = []
        for i in range(len(q)):
            
            node = q.pop(0)    
            subresult.append(node.data)
            # print(node.data)
            if node.left != None:
                q.append(node.left)
            if node.right != None:
                q.append(node.right)
        result.append(subresult)
    print(result)
def LeftView(root):
    result = []
    q = [root]
    if root == None:
        return result
    while q:
        n = len(q)
        for i in range(n):
            node = q.pop(0)
            # For RightView " i == n-1 " 
            if i == 0:  
                result.append(node.data)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return result
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
# Inorder(n1)
# Preorder(n1)
# Postorder(n1)
# LevelOrder(n1)
print(LeftView(n1))

Link = " https://pastebin.com/b3Xw97sX "
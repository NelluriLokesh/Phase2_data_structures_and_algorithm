class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def insertBst(root,data):
    if root == None:
        return Node(data)
    elif root.data < data :
        root.right = insertBst(root.right,data)
    elif root.data > data :
        root.left = insertBst(root.left,data)
    return root
def searchBst(root,target):
    if root == None:
        return None
    if root.data == target:
        return root
    elif root.data < target :
        return searchBst(root.right,target)
    elif root.data > target :
        return searchBst(root.left,target)
def successor(root):
    root = root.right
    while root.left != None:
        root = root.left
    return root
def deleteBst(root,target):
    if root == None:
            return None
    elif root.data < target :
        root.right = deleteBst(root.right,target)
    elif root.data > target :
        root.left = deleteBst(root.left,target)
    else :
        if root.left == None and root.right == None:
            return None
        elif root.left == None:
            return root.right
        elif root.right == None:
            return root.left
        else:
            temp = root.right
            while temp.left != None:
                temp = temp.left
            root.data = temp.data
            root.right = deleteBst(root.right,temp.data)
    return root
def Inorder(root): # Do Leetcode Problems 
    if root == None:
        return
    Inorder(root.left)
    print(root.data,end = ' ')
    Inorder(root.right)
root = None
root = insertBst(root,10)
root = insertBst(root,8)
root = insertBst(root,15)
# print(searchBst(root,8))
Inorder(root)
print()
root = deleteBst(root,15)
Inorder(root)
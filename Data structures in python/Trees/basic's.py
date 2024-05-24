# class BST():
#   def __init__(self,key) -> None:
#     self.left = None
#     self.key = key
#     self.right = None
    
#   def insertion(self,data):
#     new_node = BST(key=data)
#     if self.key == None:
#       self.key = data  
    
#     elif self.key != None:
#       n = self.key
#       while n != None:
#         if data > n:
#           n = n.right
#         else:
#           n = n.left
#       if data > n:
#         n.right = new_node
#       else:
#         n.left = new_node
          
          
        
# root = BST(10)
# root.insertion(20)
# root.insertion(4)

# # print(root.data)
# # print(root.left)
# # print(root.right)

# # root.left = BST(5)

# # print(root.left.data)
# # print(root.left.right)
# # print(root.left.left)

# # root.right = BST(15)
# # print(root.right.data)
# # print(root.right.right)
# # print(root.right.left)



# # gain = [-5,1,5,0,-7]


lists = [1,2,3,4,45,5,64,43]
target = 5

count = 0
for i in range(len(lists)):
  if lists[i] == target:
    break
  else:
    count += 1
print(count)

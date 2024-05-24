
class Node:
  def __init__(self,data) -> None:
    self.data = data
    self.ref = None
    
class Linked_list():
  def __init__(self) -> None:
    self.head = None
  
  def At_Beginning(self,data):
    new_node = Node(data)
    new_node.ref = self.head 
    self.head = new_node
  
  def Traversal(self):
    if self.head is None:
      print("the lInked_list is empty")
    
    elif self.head is not None:
      n = self.head
      while n is not None:
        print(n.data)
        n = n.ref  
    
ll = Linked_list()

for i in range(4):
  ll.At_Beginning(i)

ll.Traversal()
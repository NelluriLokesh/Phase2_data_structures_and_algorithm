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
  
  def using_indexing(self,index,data):
    new_node = Node(data=data)
    if self.head is None:
      self.head = new_node
    
    elif self.head is not None:
      n = self.head
      for i in range(index):
        n = n.ref
      new_node.ref = n.ref
      n.ref = new_node
    
  def using_data(self,val,data):
    new_node = Node(data=data)
    if self.head is None:
      self.head = new_node
    
    elif self.head is not None:
      n = self.head
      while n.data != val:
        n = n.ref
      new_node.ref = n.ref
      n.ref = new_node
        
    

  def Traversal(self):
    if self.head is None:
      print("the lInked_list is empty")
    
    elif self.head is not None:
      n = self.head
      while n is not None:
        print(n.data)
        n = n.ref 
         
ll = Linked_list()

ll.At_Beginning(10)
ll.At_Beginning(20)
ll.At_Beginning(30)
ll.At_Beginning(40)
ll.At_Beginning(50)
ll.using_data(50,21)

ll.Traversal()
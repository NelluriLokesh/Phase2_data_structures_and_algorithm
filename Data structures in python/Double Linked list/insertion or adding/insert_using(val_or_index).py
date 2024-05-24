

class Node():
  def __init__(self,data) -> None:
    self.prev = None
    self.data = data
    self.next = None

class Double_linked_list:
  def __init__(self) -> None:
    self.head = None
  
  def at_begin(self,data):
    new_node = Node(data=data)
    if self.head is None:
      self.head = new_node
    else:
      new_node.next = self.head
      self.head.prev = new_node
      self.head = new_node
  
  def using_index(self,index,data):
    new_node = Node(data=data)
    if self.head == None:
      self.head = new_node
    
    else:
      n = self.head
      for i in range(index):
        n = n.next
      new_node.prev = n
      new_node.next = n.next
      n.next = new_node
      
  def using_valu(self,val,data):
    
    new_node = Node(data=data)
    if self.head == None:
      self.head = new_node
    else:
      n = self.head
      while n.data != val:
        n = n.next
      
      new_node.prev = n
      new_node.next = n.next
      n.next = new_node
      
  def Traversal(self):
    if self.head == None:
      print("there is no data in the double linked List!!!")
    else:
      n = self.head
      while n != None:
        print(n.data)
        n = n.next




dl = Double_linked_list()
for i in range(4):
  
  dl.at_begin(i)
  

dl.Traversal()


dl.using_index(1,34)

dl.Traversal()

dl.using_valu(3,35)
dl.Traversal()
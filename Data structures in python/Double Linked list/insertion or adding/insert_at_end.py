

class Node():
  def __init__(self,data) -> None:
    self.prev = None
    self.data = data
    self.next = None

class Double_linked_list:
  def __init__(self) -> None:
    self.head = None
  
  def at_ending(self,data):
    new_node = Node(data=data)
    if self.head == None:
      self.head = new_node
    
    else:
      n = self.head
      while n.next != None:
        n = n.next
      new_node.prev = n
      n.next = new_node
  
  def Traversal(self):
    if self.head == None:
      print("there is no data in the linked list!!")
    else:
      n = self.head
      while n != None:
        print(n.data)
        n = n.next
        
  def back_traversal(self):
    if self.head == None:
      print("there is not data in the double linked list")
    else:
      n = self.head
      while n.next != None:
        n = n.next
      while n != None:
        print(n.data)
        n = n.prev

dl = Double_linked_list()
for i in range(4):
  dl.at_ending(i)
  
dl.Traversal()

print("back traversal::")
dl.back_traversal()
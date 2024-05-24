

class Node:
  def __init__(self,data) -> None:
    self.data = data
    self.ref = None

class Linked_list():
  def __init__(self) -> None:
    self.head = None
  
  def At_endding(self,data):
    new_data = Node(data)
    if self.head is None:
      self.head = new_data
    elif self.head is not None:
      n = self.head
      while n.ref is not None:
        n = n.ref
      n.ref = new_data
      
  def traversal(self):
    if self.head == None:
      print("the linked_list empty")
    else:
      n = self.head
      while n is not None:
        print(n.data)
        n = n.ref

ll = Linked_list()

for i in range(4):
  ll.At_endding(i)

ll.traversal()




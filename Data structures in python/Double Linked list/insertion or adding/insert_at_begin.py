class Node:
  def __init__(self,data) -> None:
    self.prev = None
    self.data = data
    self.next = None
class double_linked_list:
  def __init__(self) -> None:
    self.head = None
  
  def adding_begin(self,data):
    new_node = Node(data)
    if self.head == None:
      self.head = new_node
    else:
     new_node.next = self.head
     self.head.prev = new_node
     self.head = new_node
  
  
  def traversal(self):
    n = self.head
    while n != None:
      print(n.data)
      n = n.next
      
  def back_traversal(self):
    if self.head == None:
      print("there is no data in dl")
    else:
      n = self.head
      while n.next is not None:
        n = n.next
      while n != None:
        print(n.data)
        n = n.prev
        
    
    
ll = double_linked_list()

for i in range(4):
  ll.adding_begin(i)

ll.adding_begin(5)

ll.traversal()

print("back::")
ll.back_traversal()

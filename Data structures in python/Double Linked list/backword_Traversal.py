
class node:
  def __init__(self,data) -> None:
    self.prev = None
    self.data = data
    self.next = data

class Double_linked_list:
  def __init__(self) -> None:
    self.head = None
  
  
        
  def backward_traversal(self):
    if self.head == None:
      print("the dll is empty.!!")
    else:
      n = self.head
      while n.next != None:
        n = n.next
      while n is not None:
        print(n.data)
        n = n.prev
      
    
dl = Double_linked_list()

dl.forward_Traversal()
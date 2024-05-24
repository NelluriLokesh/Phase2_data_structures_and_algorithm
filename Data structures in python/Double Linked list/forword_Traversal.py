
class node:
  def __init__(self,data) -> None:
    self.prev = None
    self.data = data
    self.next = data

class Double_linked_list:
  def __init__(self) -> None:
    self.head = None
  
  
  def forward_Traversal(self):
    if self.head == None:
      print("the dll is empty..!!")
    else:
      n = self.head
      while n != None:
        print(n.data)
        n = n.next
      
      
    
dl = Double_linked_list()

dl.forward_Traversal()
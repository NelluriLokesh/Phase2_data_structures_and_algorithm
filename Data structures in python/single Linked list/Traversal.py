

# creating an node 
class node():
  def __init__(self,data) -> None:
    self.data = data
    self.ref = None
    
class linked_list:
  def __init__(self) -> None:
    self.head = None
  
  def adding(self,data):
    new_data = node(data)
    new_data.ref = self.head
    self.head = new_data
    
    
  def Traversal(self):
    
    if self.head is None:
      print("The linked list is empty....!!! ")
    
    elif self.head is not None:
      n = self.head
      
      while n is not None:
        print(n.data)
        n = n.ref
        
  def back_traver(self):
    
    n = self.head 
        
ll = linked_list()
for i in range(6):  
  ll.adding(i)    
ll.Traversal()         
  





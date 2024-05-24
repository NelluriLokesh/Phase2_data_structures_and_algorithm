# user_input = input("Enter data either an integer or a character: ")
# data = None
# if user_input.isdigit():
#     val = int(user_input)
#     data = val
# else:
#     char = user_input
#     data = char
    
# print(data)
# print(type(data))

class double_Node:
  def __init__(self,data) -> None:
    self.prev = None
    self.data = data
    self.next = None
class double_linked_list():
  def __init__(self) -> None:
    self.head = None
  
  def At_begin(self,data):
    new_node = double_Node(data=data)
    if self.head == None:
      self.head = new_node
    else:
      new_node.next = self.head
      self.head.prev = new_node
      self.head = new_node
  
  def At_ending(self,data):
    new_node = double_Node(data=data)
    if self.head == None:
      self.head = new_node
    else:
      n = self.head
      while n.next != None:
        n = n.next
      new_node.prev = n
      n.next = new_node
      
  def adding_middle_using_index(self,index,data):
    new_node = double_Node(data)
    if self.head == None:
      self.head = new_node
    else:
      n = self.head
      for i in range(index):
        n = n.next
      new_node.next = n.next
      new_node.prev = n
      n.next.prev = new_node
      n.next = new_node
  
  def delete_begin(self):
    if self.head == None:
      print("there is no data to delete!!")
    else:
      self.head.prev = None
      self.head = self.head.next
      
  def delete_ending(self):
    if self.head == None:
      print("there is no data to delete!!")
    else:
      n = self.head
      while n.next.next != None:
        n = n.next
      n.next = None
  def delete_using_index(self,index):
    
    indexs = []
    r = self.head
    while r != None:
      indexs.append(r.data)
      r = r.next
    count = len(indexs)
    if count < index:
      print("the index is out of range!!")
    
    elif index == 0:
      self.head = self.head.next
    else:
      n = self.head
      for i in range(index-1):
        n = n.next
      n.next = n.next.next
      n.next.prev = n
    

    
    
  def forward_traversal(self):
    if self.head == None:
      print("there is no data in the double linked list")
    else:
      n = self.head
      while n != None:
        print(n.data)
        n = n.next
  def backward_traversal(self):
    if self.head == None:
      print("the double lined list empty!!")
    else:
      n = self.head
      while n.next != None:
        n = n.next
      while n != None:
        print(n.data)
        n = n.prev

class Queues_using_double_linked_list():
  def __init__(self) -> None:
    self.head = None
  
  def putt(self,data):
    new_data = double_Node(data=data)
    if self.head == None:
      self.head = new_data
    else:
      n = self.head
      while n.next != None:
        n = n.next
      n.next = new_data
      new_data.prev = n
      
  def poping(self):
    if self.head == None:
      print("there is no data to pop from the queues!!")
    elif self.head.next == None:
      self.head = None
    else:
      self.head = self.head.next
    
      
  def forward_traversal(self):
    if self.head == None:
      print("there is no data in the double linked list")
    else:
      n = self.head
      while n != None:
        print(n.data)
        n = n.next

class Stack_using_double_linked_list():
  def __init__(self) -> None:
    self.head = None
  
  def appending(self,data):
    new_data = double_Node(data=data)
    if self.head == None:
      self.head = new_data
    else:
      n = self.head
      while n.next != None:
        n = n.next
      new_data.prev = n
      n.next = new_data
  def popp(self):
    if self.head == None:
      print("there is no data in stack!!")
    else:
      n = self.head
      while n.next.next != None:
        n = n.next
      n.next = None
    
  def traversal(self):
    if self.head is None:
        print("There is no data present in the stack")
        return 0

    n = self.head
    elements = []

    while n is not None:
        elements.append(str(n.data))
        n = n.next

    dash_line = '-' * (3 * len(elements) + len(elements) - 1)
    print(dash_line)
    print(f"| {' | '.join(elements)} ")

    print(dash_line)
    return len(elements)


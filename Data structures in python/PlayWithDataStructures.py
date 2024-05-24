# from utitles import *

import collections
import queue


class lists():
  def __init__(self) -> None:
    self.list_data = collections.deque()
  def appending(self,data):
    self.list_data.append(data)
    print(self.list_data)
    
  def poping(self):
    if len(self.list_data) == 0:
      print("the list is empty!!")
    
    else:
      print("before poping : ",self.list_data)

      self.list_data.pop()
    
      print("after poping : ",self.list_data)


class Stack():
  def __init__(self) -> None:
    self.stack_data = collections.deque()
  def push(self,element):
    
    self.stack_data.append(element)
    print(self.stack_data)

  def popp(self):
    if len(self.stack_data) == 0:
      print("the stack is empty..")
    else:
      self.stack_data.pop()
      print(self.stack_data)

class queues():
  def __init__(self) -> None:
    self.queues_data = []
  def push(self,element):
    
    self.queues_data.append(element)
    print(self.queues_data)

  def popp(self):
    if len(self.queues_data) == 0:
      print("the stack is empty..")
    else:
      self.queues_data.pop(0)
      print(self.queues_data)
    
    
class Node():
  def __init__(self,data) -> None:
    self.data = data
    self.next = None

class Linked_list():
  def __init__(self) -> None:
    self.head = None
  
  ## Insertion of the data

  ## Adding at data at beginning of the linked list
  def At_begin(self,data):
    new_data = Node(data=data)
    new_data.next = self.head
    self.head = new_data
    
  ## Adding at the middle using the index value
  def using_index(self,index,data):
    new_node = Node(data)
    total = []
    r = self.head
    while r is not None:
      total.append(r)
      r = r.next
    count = len(total)
    if count < index:
      print("the index values is out of range!!!")
      chh = int(input("""
            select
            1. to add at the begin of the linked list
            2.to add at the ending of the linked list
            4.to no adding"""))
      if chh == 1:
        new_node.next = self.head
        self.head = new_node
      elif chh == 2:
        if self.head is not None:
          n = self.head
          while n.next != None:
            n = n.next
          new_node.next = n.next
          n.next = new_node
        elif self.head == None:
          self.head = new_node
          
      else:
        return
      
    elif count > index:
      n = self.head
      for i in range(index):
        n = n.next
      new_node.next = n.next
      n.next = new_node
  
  ## Adding at the middle using the before value
  def using_data(self,val,data):
    new_node = Node(data=data)
    n = self.head
    while n.data != val:
      n = n.next
    new_node.next = n.next
    n.next = new_node
    
  ## Adding at the end of the linked list
  def appending_At_end(self,data):
    new_data = Node(data=data)
    if self.head is None:
      self.head = new_data
    else:
      n = self.head
      while n.next is not None:
        n = n.next
      n.next = new_data
  
  ## Delection of the data
  
  ## deleting the data at the begin
  def del_Begin(self):
    if self.head == None:
      print('there is no data to delete!!')
    else:
      self.head = self.head.next
  
  ## deleting at the middle using index val
  
  def del_using_index(self,index):
    val = []
    r = self.head
    while r != None:
      val.append(r.data)
      r = r.next
    length = len(val)
    if length < index:
      print("the index is out of range...!!")
    else:
      if self.head == None:
        print("there is no data to delete..!!")
      elif self.head.next == None:
        self.head = None
      else:
        if index == 0:
          self.head = self.head.next
        else:
          n = self.head
          for i in range(index - 1):
            n = n.next
          n.next = n.next.next
  
  
  def del_end(self):
    if self.head == None:
      print("the list is empty..")
    
    elif self.head.next is None:
      self.head = None
    
    else:
      n = self.head
      while n.next.next != None:
        n = n.next
      n.next = None
      
  

## Printing all the data presented in the linked list
  def Traversal(self):
    if self.head is None:
      print("the lInked_list is empty")
    
    elif self.head is not None:
      n = self.head
      while n is not None:
        print(n.data,end="-->")
        n = n.next
      print('None')

class Stack_using_linkedList():
  def __init__(self) -> None:
    self.head = None
    
  def pushing(self,data):
    new_data = Node(data=data)
    if self.head == None:
      self.head = new_data
    else:
      n = self.head
      while n.next !=None:
        n = n.next
      new_data.next = n.next
      n.next = new_data
      
  def Poping(self):
    if self.head == None:
      print("there is no data to pop")
    elif self.head.next == None:
      self.head = None
    else:
      n = self.head
      while n.next.next != None:
        n = n.next
      n.next = None
    
    
  def Traversal(self):
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

class Queues_using_linkedList():
  def __init__(self) -> None:
    self.head = None
  
  def put(self,data):
    new_data = Node(data=data)
    if self.head == None:
      self.head = new_data
    else:    
      n = self.head
      while n.next != None:
        n = n.next
      new_data.next = n.next
      n.next = new_data
  

  
  def get(self):
    if self.head == None:
      return
    else:
      self.head = self.head.next
      
  def traversal(self):
    if self.head is None:
        print("There is no data present in the queues \n")
        return 0

    n = self.head
    elements = []

    while n is not None:
        elements.append(str(n.data))
        n = n.next

    dash_line = '-' * (3 * len(elements) + len(elements) - 1)
    print(dash_line)
    print(f" {' | '.join(elements)} ")

    print(dash_line)
    return len(elements)

class double_Node():
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
  
  def forward_traversal(self):
    if self.head == None:
      print("there is no data in double linked list")
    else:
      n = self.head
      while n != None:
        print(n.data)
        n = n.next
    
  def back_traversal(self):
    if self.head == None:
      print("the double linked list is empty!!")
    else:
      n = self.head
      while n.next != None:
        n = n.next
      while n!= None:
        print(n.data)
        n = n.prev
  
  def adding_using_index(self,index,data):
    new_node = double_Node(data=data)
    if self.head == None:
      self.head = new_node
    else:
      n = self.head 
      for i in range(index):
        n = n.next
      new_node.next = n.next
      new_node.prev = n
      n.next = new_node
      n.next.prev = new_node
      
  def delete_begin(self):
    if self.head == None:
      print("No data to delete!!")
    else:
      self.head.prev = None
      self.head = self.head.next
  
  def delete_ending(self):
    if self.head == None:
      print("no data to delete!!")

    elif self.head.next == None:
      self.head = None
    else:
      n = self.head
      while n.next.next != None:
        n = n.next
      n.next = None
      
  def delete_using_index(self,index):
    ind = 0
    r = self.head
    while r != None:
      ind += 1
      r = r.next
    
    if ind < index:
      print("the given index is out of range!!")
    elif index == 0:
      self.head = self.head.next
    else:
      n = self.head
      for i in range(index - 1):
        n = n.next
      n.next = n.next.next
      n.next.prev = n

class Queues_using_double_linked_list():
  def __init__(self) -> None:
    self.head = None
  
  def pushing(self,data):
    new_data = double_Node(data=data)
    if self.head == None:
      self.head = new_data
    else:
      n = self.head
      while n.next != None:
        n = n.next
      new_data.prev = n
      n.next = new_data
      
  def poping(self):
    if self.head == None:
      print("there is no data to pop from queues")
    elif self.head.next == None:
      self.head = None
    else:
      self.head = self.head.next
      
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
    print(f" {' | '.join(elements)} ")

    print(dash_line)
    return len(elements)
    
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
    elif self.head.next == None:
      self.head = None
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



user_input = input("""
  play with :: \n
  1.list (l or 1)
  2.stack (s or 2)
  3.queues (q)
  4.single Linked lists (single linked list,stack,queues)
  5.Double Linked Lists (double , list, queues using double linked list)
  6.Trees 
  
  
  select : 
  """)
user  = None
if user_input.isdigit():
    val = int(user_input)
    user = val
else:
    char = user_input
    user = char
    



if user in ('l','L',1):
  
  print("\n          > list <              \n ")
  
  li = lists()
  while True:
    
    chhh = int(input("select \n 1.append \n 2.pop \n 3.show the list \n 4.exit"))
    if chhh == 1:
      user_input = input("Enter data to insert into List..: ")
      data = None
      if user_input.isdigit():
          val = int(user_input)
          data = val
      else:
          char = user_input
          data = char
      
      li.appending(data=data)
    elif chhh== 2:
      li.poping()
    elif chhh == 3:
      print(li.list_data)
    elif chhh == 4:
      break

      
        
elif user in ('s',2):
  print("\n                    > Stack <                     \n")
  sta = Stack()
  
  while True:
    choies = int(input("select one in \n 1.push\n 2.pop\n 3.show data of stack\n \n 4.exit ..."))
    if choies ==1:
      user_input = input("Enter data either an integer or a character: ")
      data = None
      if user_input.isdigit():
          val = int(user_input)
          data = val
      else:
          char = user_input
          data = char
      sta.push(data)

    elif choies == 2:
      if len(sta.stack_data) == 0:
        print("there no data to pop")
      else:
        sta.popp()
    elif choies == 3:
      print(sta.stack_data)
    elif choies == 4:
      break
  
elif user in ('q','Q',3):
  
  print("\n          > Queues using List<            \n")
  
  que = queues()
  while True:
    choies = int(input("select one in \n 1.push\n 2.pop\n 3.show data of queues\n \n 4.exit ..."))
    if choies ==1:
      user_input = input("Enter data either an integer or a character: ")
      data = None
      if user_input.isdigit():
          val = int(user_input)
          data = val
      else:
          char = user_input
          data = char
      que.push(data)

    elif choies == 2:
      if len(que.queues_data) == 0:
        print("there no data to pop")
      else:
        que.popp()
    elif choies == 3:
      print(que.queues_data)
    elif choies == 4:
      break
  
  
elif user in ("LL",'ll','Ll',"lL",4):
  
  types_in_link = int(input("""select 
             1.single linked list  (ll or 1) \n 
             2.stack using linked list (sl or 2) \n 
             3.Queues using linked list (ql or 3)"""))
  if types_in_link == 1:
    
    print("\n                      > Linked list <                    \n ")
    ll = Linked_list()

    while True:
      
      cho = int(input("""
      select \n 
      1.Adding data at begin \n 
      2.adding data at ending \n 
      3.insert data using indexing \n 
      4.insert data using before data \n 
      5.delete the data at begin \n 
      6.delete the node at ending \n 
      7.to delete the data using index \n 
      8.to see the data \n 
      9.exit """))
      
      if cho == 1:
        
        print("after adding :")
        ll.Traversal()
        
        # data = int(input('enter the data : '))
        user_input = input("Enter data either an integer or a character: ")
        data = None
        if user_input.isdigit():
            val = int(user_input)
            data = val
        else:
            char = user_input
            data = char
            
        ll.At_begin(data=data)
        
        
        print("after adding at begin :")
        ll.Traversal()
      
      elif cho == 2:
        print("the linked list : ")
        ll.Traversal()
        
        user_input = input("Enter data either an integer or a character: ")
        data = None
        if user_input.isdigit():
            val = int(user_input)
            data = val
        else:
            char = user_input
            data = char
            
        ll.appending_At_end(data=data)
        
        print("after adding at ending :")
        ll.Traversal()
        
      
      elif cho == 3:
        print("the data in the linked list :: ")
        ll.Traversal()
        index = int(input('enter the index : '))

        user_input = input("Enter data either an integer or a character: ")
        data = None
        if user_input.isdigit():
            val = int(user_input)
            data = val
        else:
            char = user_input
            data = char
            
        ll.using_index(index,data)
        
        print("after insertion")
        ll.Traversal()
        
      elif cho == 4:
        print("the data in the linked list :: ")
        ll.Traversal()
        user_inpu = input("Enter the before val:  ")
        val = None
        if user_inpu.isdigit():
            al = int(user_inpu)
            val = al
        else:
            char = user_inpu
            val = char
      
        
        user_input = input("Enter data either an integer or a character: ")
        data = None
        if user_input.isdigit():
            val = int(user_input)
            data = val
        else:
            char = user_input
            data = char
      
        ll.using_data(val,data)
        
        print("after the insertion")
        ll.Traversal()
      
      elif cho == 5:
        print("before the deletion :: ")
        ll.Traversal()
        ll.del_Begin()
        print("after the deletion :: ")
        ll.Traversal()
        
      
      elif cho == 6:
        print("before the deletion :: ")
        ll.Traversal()
        ll.del_end() 
        print("after the deletion :: ")
        ll.Traversal()
            
      elif cho == 7:
        print("the data in the linked list :: ")
        ll.Traversal()
        index = int(input('enter the index : '))
        ll.del_using_index(index=index)
        
        print("after deletion::")
        ll.Traversal()
        
      elif cho == 8:
        ll.Traversal()
      elif cho == 9:
        break
  elif types_in_link == 2:
    print("\n     > stack using linked list <          \n ")
    s = Stack_using_linkedList()
    # ll = Linked_list()
    while True:
      chh = int(input("select :: \n 1.push \n 2.pop \n 3.exit"))
      if chh == 1:
        
        user_input = input("Enter data either an integer or a character: ")
        data = None
        if user_input.isdigit():
            val = int(user_input)
            data = val
        else:
            char = user_input
            data = char
            
        
        s.pushing(data=data)
        
        print("the data inserted into stack ::")
        s.Traversal()
      elif chh == 2:
        print("the stack::")
        s.Traversal()
        
        s.Poping()
        
        print("after poping::")
        s.Traversal()
      elif chh == 3:
        break
  elif types_in_link == 3:

    print("\n    > Queues using linked list <       \n")
    
    que = Queues_using_linkedList()
    
    while True:
      cho = int(input("1.put \n 2.get \n 3.exit"))
      if cho == 1:
        print("the queues :")
        que.traversal()
        
        user_input = input("Enter data either an integer or a character: ")
        data = None
        if user_input.isdigit():
            val = int(user_input)
            data = val
        else:
            char = user_input
            data = char
      
        que.put(data=data)
        
        print("the queues after the put operation")
        que.traversal()
      
      elif cho == 2:
        print("the queues :")
        que.traversal()
        
        que.get()
        
        print("the queues after the get operation")
        que.traversal()
      
      elif cho == 3:
        break

elif user == 5:
  
  user_input = input("""
select 
1.double linked list... 
2.stack using double linked list
3.queues using double linked list
""")
  choies = None
  if user_input.isdigit():
      val = int(user_input)
      choies = val
  else:
      char = user_input
      choies = char
  if choies == 1:
    
    dl = double_linked_list()
    print("        > double linked_list <           ")
    
    while True:
      user = input("""
  1.adding at the begin
  2.adding at the ending
  3.adding data using the index
  4.deletion of the begin data
  5.deletion of the end data
  6.delete using indexx
  7.Forward traversal
  8.back traversal

  select :     """)
      da = None
      if user.isdigit():
          val = int(user)
          da = val
      else:
          char = user
          da = char
      

      if da in (1,'begin'):
        
        user_input = input("Enter data either an integer or a character: ")
        data = None
        if user_input.isdigit():
            val = int(user_input)
            data = val
        else:
            char = user_input
            data = char
        dl.At_begin(data)
      elif da == 2:
        user_input = input("Enter data either an integer or a character: ")
        data = None
        if user_input.isdigit():
            val = int(user_input)
            data = val
        else:
            char = user_input
            data = char
        dl.At_ending(data=data)
        
      elif da == 3:
        index = int(input("enter the before index value ::"))
        user_input = input("Enter data either an integer or a character: ")
        data = None
        if user_input.isdigit():
            val = int(user_input)
            data = val
        else:
            char = user_input
            data = char
        
        dl.adding_using_index(index=index,data=data)
      
      elif da == 4:
        dl.delete_begin()
      elif da == 5:
        dl.delete_ending()

      elif da == 6:
        user_input = input("Enter data either an integer or a character: ")
        index = None
        if user_input.isdigit():
            val = int(user_input)
            index = val
        else:
            char = user_input
            index = char
        
        dl.delete_using_index(index=index)
        
      elif da == 7:
        dl.forward_traversal()
      elif da == 8:
        dl.back_traversal()
      else:
        break 
  elif choies == 2:
    sl= Stack_using_double_linked_list()
    print("> Stack using double linked list <")
    
    while True:  
      pic = int(input("select \n 1.push \n 2.pop \n 3show the queue data \n 4.exit"))
      if pic == 1:
        user_input = input("Enter data either an integer or a character: ")
        data = None
        if user_input.isdigit():
            val = int(user_input)
            data = val
        else:
            char = user_input
            data = char
            
        sl.appending(data=data)
        sl.traversal()
      elif pic == 2:
        sl.popp()
        sl.traversal()
      elif pic == 3:
        sl.traversal()
      else:
        break
  
  elif choies == 3:
    qq = Queues_using_double_linked_list()
    print("> queues using double linked list <")
    
    while True:
      
      pic = int(input("select \n 1.push \n 2.pop \n 3show the queue data \n 4.exit"))
      
      if pic == 1:
        user_input = input("Enter data either an integer or a character: ")
        data = None
        if user_input.isdigit():
            val = int(user_input)
            data = val
        else:
            char = user_input
            data = char
            
        qq.pushing(data=data)
        qq.traversal()
      elif pic == 2:   
        qq.poping()
        qq.traversal()
      elif pic == 3:
        qq.traversal()
      else:
        break
      


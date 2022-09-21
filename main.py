class Node:
  def __init__(self, data=None, next=None, prev=None):
    self.data=data
    self.next=next
    self.prev=prev

class DoublyLinkedList:
  def __init__(self):
    self.head=None

  def insert_at_beginning(self, data):
    n=Node(data,self.head,None)
    self.head=n

  def insert_at_end(self, data):
    if self.head is None:
      self.head=Node(data,None,None)
      return
    i=self.head
    while i.next!=None:
      i=i.next
    n=Node(data, None,i)
    i.next=n

  def insert_values(self, list_data):
    for i in list_data:
      self.insert_at_end(i)

  def insert_at(self, index, data):
    if index < 0 or index>=self.get_length():
      raise Exception ("invalid index")

    if index==0:
      self.insert_at_beginning(data)

    i=self.head
    count=0
    while i:
      #node just before the node to add
      if count==index-1:
        tem=i.next
        i.next=Node(data,tem,i)
        i.next.next.prev=i.next
        break
      i=i.next
      count+=1
      

  def Clear_and_insert_values(self, list_data):
    self.head=None
    for i in list_data:
      self.insert_at_end(i)
      
  def get_length(self):
    count=0
    i=self.head
    while i:
      count+=1
      i=i.next
    return count

  def delete_at(self, index):
    if index<0 or index>=self.get_length():
      raise Exception ("invalid index")
    #starting index
    if index==0:
      self.head=self.head.next
      self.head.prev=None
      return
    count=0 
    i =self.head
    while i:
      if count==index-1:
        i.next=i.next.next
        i.next.prev=i
        break
      count+=1
      i=i.next
    
  def print(self):
    if self.head is None:
      print(" linked List is empty")
      return

    i=self.head
    llstr="" # linkedlist string 

    while i:
      llstr+=str(i.data)+"->"
      i=i.next
      
    print(llstr)# printing the final string of linkedlist

  def insert_after_value(self, data_after, data_to_insert):
    # Search for first occurance of data_after value in linked list
    # Now insert data_to_insert after data_after node
    i=self.head
    while i:
      if i.data==data_after:
        i.next=Node(data_to_insert,i.next,i)
        i.next.prev=i.next
        break
        
      i=i.next
    
  def remove_by_value(self, data):
    # Remove first node that contains data
    i=self.head
    while i.next:

      # i is the node before the node that has the "data"
      if i.next.data==data:
        #remove the node
        i.next=i.next.next
        i.next.prev=i
        break

        
  def print_forward(self):
    # This method prints list in forward direction. Use node.next
    if self.head is None:
      print(" linked List is empty")
      return

    i=self.head
    dllstr="" # linkedlist string 

    while i:
      dllstr+=str(i.data)+"->"
      i=i.next
    print(dllstr)# printing the final string of linkedlist

  
  def get_last_node(self):
    i =self.head
    while i.next:
      i=i.next
    return i
    
  def print_backward(self):
    if self.head is None:
      print(" linked List is empty")
      return
      
    # Print linked list in reverse direction. Use node.prev for this.
    last_node=self.get_last_node()
    i =last_node
    dllstr=""
    while i:
      dllstr+=str(i.data)+"->"
      i=i.prev
      print(i)
    print("in reverse order from doubly linked list",dllstr)
      

if __name__=="__main__":
  ll=DoublyLinkedList()
  ll.insert_at_beginning(3)
  ll.insert_at_beginning(5)
  ll.insert_at_beginning(3)
  ll.insert_at_end(8)
  ll.insert_values([3,4,5])
  ll.Clear_and_insert_values([3,4,5])
  ll.insert_at(2,0)
  ll.insert_after_value(3,9)
  ll.print()
  #output: 3-> 9->4->0->5

  ll.remove_by_value(9)
  ll.print_forward()
  ll.print_backward()

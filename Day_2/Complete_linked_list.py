# Node Class
class Node:
    # Constructor
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

# A Linked List class 
class LinkedList:
  def __init__(self):  
    self.head = None
  
  # insertion method 
  def insert(self, data):
    newNode = Node(data)
    # checking whether the head is empty or not
    if(self.head):
      # getting the current node
      current = self.head
      while(current.next):
        current = current.next
      # assing the new node to the next pointer
      current.next = newNode
    else:
      # if head is empty assigning the node to head
      self.head = newNode
  
  # print method 
  def printLL(self):
    # variable of iteration
    current = self.head
    
    # iteration until we reach the end of the linked list
    # while(current != None)
    while(current):      
      # print the node Data and next hash
      print("[ {} ]".format(current.data),end=" --> ")
      # Moving to the next node 
      current = current.next
    print("Null")
  
  def length(self):
      cur = self.head
      total = 0
      while (cur.next != None):
          total +=1
          cur = cur.next
      return total

  def remove(self,index):
      if index >= self.length():
          print("Error, index is out of range")
          return None
      cur_idx = 0
      cur_node = self.head
      while True:
          last_node = cur_node
          cur_node = cur_node.next 
          if cur_idx == index:
              last_node.next = cur_node.next
              return
          cur_idx += 1
  
  def get(self,index):
      if index >= self.length():
          print("Error, index is out of range")
          return None
      cur_idx = 0
      cur_node = self.head
      while True:
          cur_node = cur_node.next
          if (cur_idx == index):  return cur_node.data
          cur_idx +=1

  def pushAt(self, index,data):
      if index >= self.length():
          print("Error, index is out of range")
          return None
      objNode = Node(data)
      if(self.head):
        tmp = self.head
        counter = 0
        while(tmp !=None and counter < index):
            tmp = tmp.next
            counter +=1

        objNode.next = tmp.next
        tmp.next = objNode

        


# Singly Linked List with insertion and print methods
linked = LinkedList()
list_len = int(input("Enter List Number: "))
while(list_len > 0):
  linked.insert(input("Enter Element:"))
  list_len -=1



# Traversing
print("")
linked.printLL()


# Push Element at
push_idx = int(input("Push Index : "))
push_data = int(input("Push Element: "))
print(linked.pushAt(push_idx,push_data))

print("")
linked.printLL()


##GetElementAt Operation
get_index = int(input("Enter index number for Get Element: "))
print("Element {} at {} index:".format(linked.get(get_index),get_index))




##RemoveAt index Operation
delete_idx = int(input("Enter Index for Remove:"))
linked.remove(delete_idx)
print("After Remove Operation")
linked.printLL()
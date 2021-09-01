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
      print("[ {} | {} ]".format(current.data,id(current.next)),end=" --> ")
      # Moving to the next node 
      current = current.next
    print("Null")
# Singly Linked List with insertion and print methods
linked = LinkedList()


list_len = int(input("Enter List Number: "))


while(list_len > 0):
  linked.insert(input("Enter Element:"))
  list_len -=1



linked.printLL()

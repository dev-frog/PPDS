class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printlist(self):
        tmp = self.head
        while(tmp):
            print(tmp.data)
            tmp = tmp.next



list_1 = LinkedList()

list_1.head = Node("One")

second = Node("Two")
third = Node("Three")

list_1.head.next = second
second.next = third


list_1.printlist()


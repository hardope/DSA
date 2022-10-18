# Doubly Linked list

class Node:
     # function to initialize or create node
     def __init__(self, data):
          self.data = data
          self.next = None
          self.prev = None

class LinkedList:
     # Initialize or create empty Linked list
     def __init__(self):
          self.head = None

     # print linked list
     def print_back(self):
          if self.head is None:
               print("Linked List is Empty")
          else:
               node = self.head
               while node.next is not None:
                    node = node.next
               print("[", end="")
               while node is not None:
                    if node.prev is not None:
                         print(node.data, end=", ")
                    else:
                         print(node.data, end="")
                    node = node.prev
               print("]")
     
     def print_ll(self):
          if self.head is None:
               print("Linked List is Empty")
          else:
               node = self.head
               print("[", end="")
               while node is not None:
                    if node.next is not None:
                         print(node.data, end=", ")
                    else:
                         print(node.data, end="")
                    node = node.next
               print("]")

     # Method to Insert Node at start Of linked List
     def add_begin(self, data):
          new_node = Node(data)
          new_node.next = self.head
          self.head.prev = new_node
          self.head = new_node

     def add_empty(self, data):
          new_node = Node(data)
          self.head = new_node

     def add_end(self, data):
          new_node = Node(data)
          # Check if list is empty: If empty add as first node
          if self.head is None:
               new_node.next = self.head
               self.head = new_node
          else:
               node = self.head
               while node.next is not None:
                    node = node.next
               node.next = new_node
               new_node.prev = node

ll1 = LinkedList()
ll1.add_empty(1)
ll1.add_begin(0)
ll1.add_end(2)


ll1.print_ll()
ll1.print_back()
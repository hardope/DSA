# Singly Linked list

class Node:
     # function to initialize or create node
     def __init__(self, data):
          self.data = data
          self.ref = None

class LinkedList:
     # Initialize or create empty Linked list
     def __init__(self):
          self.head = None

     # print linked list
     def print_ll(self):
          if self.head is None:
               print("Linked List is Empty")
          else:
               node = self.head
               print("[", end="")
               while node is not None:
                    if node.ref is not None:
                         print(node.data, end=", ")
                    else:
                         print(node.data, end="")
                    node = node.ref
               print("]")

     # Insert Node at start Of linked List
     def add_begin(self, data):
          new_node = Node(data)
          new_node.ref = self.head
          self.head = new_node

     # insert Node at end of Linked List
     def add_end(self, data):
          new_node = Node(data)
          if self.head is None:
               new_node.ref = self.head
               self.head = new_node
          else:
               node = self.head
               while node.ref is not None:
                    node = node.ref
               node.ref = new_node
               
          
                    

ll1 = LinkedList()
ll1.add_begin(10)
ll1.add_end(20)
ll1.add_end(30)
ll1.add_end(40)
ll1.add_end(10)
ll1.print_ll()

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

     # Method to Insert Node at start Of linked List
     def add_begin(self, data):
          new_node = Node(data)
          new_node.ref = self.head
          self.head = new_node

     # Method to insert Node at end of Linked List
     def add_end(self, data):
          new_node = Node(data)
          # Check if list is empty: If empty add as first node
          if self.head is None:
               new_node.ref = self.head
               self.head = new_node
          else:
               node = self.head
               while node.ref is not None:
                    node = node.ref
               node.ref = new_node

     def add_mid(self, data, pos, x):
          # pos parameter: to determine where to add new node aither before or after
          # x parameter: The value of the selected reference node
          new_node = Node(data)
          if pos == 0:
               # add before
               pass
          
          else:
               # add after
               node = self.head
               while node is not None:
                    if node.data == x:
                         break
                    node = node.ref
               if node == None:
                    print("Node Not Found")
               else:
                    new_node.ref = node.ref
                    node.ref = new_node

     

               
          
                    
# Initialize linked list using class

ll1 = LinkedList()
ll1.add_mid(2, 1, 25)

# add data to list
ll1.add_begin(10)
ll1.add_end(20)
ll1.add_end(30)
ll1.add_end(40)
ll1.add_end(10)

ll1.add_mid(1, 1, 40)
ll1.add_mid(2, 1, 20)

# Test node not found
ll1.add_mid(2, 1, 25)
ll1.add_mid(2, 1, 40)
ll1.add_mid(8, 1, 10)

# Print List
ll1.print_ll()

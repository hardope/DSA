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

     def add_before(self, data, x):
          # x parameter: The value of the selected reference node
          if self.head == None:
               # if linked list is empty
               print("Lined List Is empty")
               return
          if x == self.head.data:
               # if add position falls on start point
               add_begin(data)
               return
          else:
               new_node = Node(data)
               node = self.head
               while node.ref is not None:
                    if node.ref.data == x:
                         break
                    node = node.ref
               if node == None:
                    print("Node Not Found")
               
               new_node.ref = node.ref
               node.ref = new_node
               
               
     def add_after(self, data, x):
          # add after
          new_node = Node(data)
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

     def add_empty(self, data):
          if self.head != None:
               print("Linked List Not Empty")
          else:
               new_node = Node(data)
               self.head = new_node

     # Delete from beginning
     def del_begin(self):
          if self.head == None:
               print("Linked is Empty")
          else:
               self.head = self.head.ref

     def del_end(self):
          if self.head == None:
               print("Linked is Empty")
          else:
               node = self.head
               while node.ref.ref is not None:
                    node = node.ref
               node.ref = None

     def del_before(self, x):
          if self.head == None:
               print("Linked is Empty")
          else:
               node = self.head
               while node.ref is not None:
                    if node.ref.ref.data == x:
                         break
                    node = node.ref
               if node == None:
                    print("Node Not Found")
               else:
                    node.ref = node.ref.ref
     
     def del_after(self, x):
          if self.head == None:
               print("Linked is Empty")
          else:
               node = self.head
               while node.ref is not None:
                    if node.data == x:
                         break
                    node = node.ref
               if node == None:
                    print("Node Not Found")
               else:
                    print(node.data)
                    node.ref = node.ref.ref
          
     

               
          
                    
# Initialize linked list using class

ll1 = LinkedList()

ll1.add_empty(1)
ll1.add_begin(0)
ll1.add_after(2, 1)
ll1.add_end(4)
ll1.add_before(3, 4)
#ll1.del_begin()
#ll1.del_end()
#ll1.del_before(4)
ll1.del_after(2)



# Print List
ll1.print_ll()

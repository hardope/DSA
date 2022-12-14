# Singly Linked list

class Node:
     # function to initialize or create node
     def __init__(self, data):
          self.data = data
          self.next = None

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
          self.head = new_node

     # Method to insert Node at end of Linked List
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

     def add_before(self, data, x):
          # x parameter: The value of the selected nexterence node
          if self.head == None:
               # if linked list is empty
               print("Lined List Is empty")
               return
          if x == self.head.data:
               # if add position falls on start point
               self.add_begin(data)
               return
          else:
               new_node = Node(data)
               node = self.head
               while node.next is not None:
                    if node.next.data == x:
                         break
                    node = node.next
               if node == None:
                    print("Node Not Found")
               
               new_node.next = node.next
               node.next = new_node
               
               
     def add_after(self, data, x):
          # add after
          new_node = Node(data)
          node = self.head
          while node is not None:
               if node.data == x:
                    break
               node = node.next
          if node == None:
               print("Node Not Found")
          else:
               new_node.next = node.next
               node.next = new_node

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
               self.head = self.head.next

     # Delete from end of linked list
     def del_end(self):
          if self.head == None:
               print("Linked is Empty")
          elif self.head.next == None:
               self.head = None
          else:
               node = self.head
               while node.next.next is not None:
                    node = node.next
               node.next = None

     # Delete before a specific node
     def del_before(self, x):
          if self.head == None:
               print("Linked is Empty")
          else:
               node = self.head
               while node.next is not None:
                    if node.next.next.data == x:
                         break
                    node = node.next
               if node == None:
                    print("Node Not Found")
               else:
                    node.next = node.next.next
     
     # Delete after a specific Node
     def del_after(self, x):
          if self.head == None:
               print("Linked is Empty")
          else:
               node = self.head
               while node.next is not None:
                    if node.data == x:
                         break
                    node = node.next
               if node == None:
                    print("Node Not Found")
               else:
                    node.next = node.next.next

     # delete specific node using value of data field     
     def del_node(self, data):
          if self.head == None:
               print("Linked is Empty")

          elif self.head.data == data:
               self.head = self.head.next
          else:
               node = self.head
               while node.next is not None:
                    if node.next.data == data:
                         break
                    node = node.next
               if node.next == None:
                    print("Node Not Found")
               else:
                    node.next = node.next.next

     

               
          
                    
# Initialize linked list using class

ll1 = LinkedList()

# Add or delete Elements
ll1.add_empty(1)
#ll1.add_begin(0)
#ll1.add_after(2, 1)
#ll1.add_end(4)
#ll1.add_before(3, 4)
ll1.add_end(5)
#ll1.del_begin()
#ll1.del_end()
#ll1.del_before(4)
#ll1.del_after(1)
ll1.del_node(1)
#ll1.del_node(2)
ll1.add_before(0, 5)



# Print List
ll1.print_ll()

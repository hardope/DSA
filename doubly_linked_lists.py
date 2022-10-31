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
          if self.head is None:
               self.head = new_node
          else:
               new_node.next = self.head
               self.head.prev = new_node
               self.head = new_node

     # Add to empty list
     def add_empty(self, data):
          if self.head is None:
               new_node = Node(data)
               self.head = new_node
          else:
               print("Linked List is not Empty")

     # Add to end of list
     def add_end(self, data):
          new_node = Node(data)
          # Check if list is empty: If empty add as first node
          if self.head is None:
               self.head = new_node
          else:
               node = self.head
               while node.next is not None:
                    node = node.next
               node.next = new_node
               new_node.prev = node
     def add_after(self, data, x):
          if self.head is None:
               print("Linked List Is empty.")
          else:
               node = self.head
               while node.next is not None:
                    if node.data == x:
                         break
                    node = node.next
               if node is None:
                    print("Node is Not present in list")
               else:
                    new_node = Node(data)
                    new_node.next = node.next
                    new_node.prev = node
                    if node.next is not None:
                         node.next.prev = new_node
                    node.next = new_node

     def add_before(self, data, x):
          if self.head is None:
               print("Linked List Is empty.")
          else:
               node = self.head
               while node is not None:
                    if node.data == x:
                         break
                    node = node.next
               if node is None:
                    print("Node is Not present in list")
               else:
                    new_node = Node(data)
                    new_node.next = node
                    new_node.prev = node.prev
                    if node.prev is not None:
                         node.prev.next = new_node
                    else:
                         self.head = new_node
                    node.prev = new_node

     def del_begin(self):
          if self.head is None:
               print("Linked List is empty.")
               return
          self.head = self.head.next
          self.head.prev = None

     def del_end(self):
          if self.head is None:
               print("Linked List is empty.")
               return
          node = self.head
          while node.next.next is not None:
               node = node.next
          node.next = None

     def del_node(self, data):
          if self.head is None:
               print("Linked List is empty.")
               return
          if self.head.data == x:
               self.head = None
          node = self.head
          while node.next is not None:
               if node.next.data == data:
                    break
               node = node.next
          node.next = node.next.next
          node.next.next.prev = node.next

ll1 = LinkedList()
ll1.add_empty(1)
ll1.add_begin(0)
ll1.add_end(2)
ll1.add_end(3)
ll1.add_end(4)
ll1.add_end(5)
ll1.del_begin()
ll1.del_end()
ll1.add_after(10, 3)
ll1.add_before(8, 1)
ll1.add_before(1, 9)
ll1.add_before(9, 2)
#ll1.del_node(3)

ll1.print_ll()
ll1.print_back()
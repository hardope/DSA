from linked_list import *

# tortise and hare algorithm to locate a node n position from end of linked list
def tortise_hare(l_list, n):
     i = 1
     # set hare and tortise and hare to first node
     hare = l_list.head
     tortise = l_list.head

     # give the hare a head start for n value
     while i < n:
          i+=1
          hare = hare.next
     
     # continue traversing until hare reached the end of linked list
     # Then current node on tortise is required node
     while hare.next is not None:
          hare = hare.next
          tortise = tortise.next

     # print required node
     print(tortise.data)

# Create linked list and add nodes
linked_list1 = LinkedList()
linked_list1.add_begin(0)
linked_list1.add_end(1)
linked_list1.add_end(2)
linked_list1.add_end(3)
linked_list1.add_end(4)
linked_list1.add_end(5)

# print linked list
linked_list1.print_ll()

# get node n position from the end of linked list
tortise_hare(linked_list1, 3)
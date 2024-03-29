# Data Structure And Algorithms

## Data structures
### Built in
* Lists
* Tuple
* Dictionary
* Sets

### User Defined
* Stack
* Queue
* Linked Lists
* Graphs
* Trees

## Lists
This is a data structure in Python that is a mutable, or changeable, ordered sequence of elements.
### Attributes
* Mutable: Can be changed or altered after initialization
* element are accessed by index
* 0 Indexed: can be indexed to get element starting from 0
* Lists are ordered
* Dynamic: Grows and shrinks in effect to data added and deleted
* Nested: list can be inside of lists

#### Example: 
list_name = [1, 2, 3, 4, 5]

## Tuple
This is similar to list and is used to store multiple items in a single variable.

### Attributes
* Immutable: Cannot be modified after initialization
* Only supports immutable Datatypes
* Nested: Tuples Can be inside other tuples

#### Example: 
tuple_name = (1, 2, 3, 4, 5)

## Dictionary
This is an unordered and mutable Python container that stores mappings of unique keys to element

### Attributes
* Mutable: Can Be edited after initialization
* Keys are Unique
* keys are immutable

#### Example: 
dictionary_name = {"key1": value, "key2": value2}

## Set
A set is a collection which is unordered, unchangeable, and unindexed.

### Attributes
* immutable: Can not Be edited after initialization
* Distinct: ommits repititions and has no duplicates
* Unordered

#### Example: 
set_name = {value1, value2}

## Stack
Stack is a linear data structure which follows a particular order in which the operations are performed. The order may be LIFO(Last In First Out) or FILO(First In Last Out)<br>
End where element are added is called top and opposite end is called base

### Operations
* Push: adding element to the top of the stack
* pop: removing element from top
* peek or top: return the top element
* isEmpty: Check sif stack is empty 

### Implementation
* List
* Modules

#### Implementing Stack using lists
* Push operation: list append function
* pop operation: list pop function

#### Implementing Stack using Modules
* Collections Module(deque class)
deque class in collection module has the pop and append function enabling use in the stack data type

* Queue Module(Lifo Queue)
     - For push operation "put" method is used
     - For pop operation "get" method is used
     - isempty: isempty function
     - isfull: isfull function
     - Limit can be set bu putting the limit value in the parenthesis when initializing stack

##### Caution if you try to pop from an empty stack you'll need to set a timeout parameter

## Queue
This is a linear data structure that is open at both ends and the operations are performed in First In First Out (FIFO) last in last out(LILO) order. Elements are added at one end(rear, back or tail) and removed from the opposite(head, front) end.

### Attributes
* LILO or FIFO
* enque: Adding element to queue
* deque: Removing element from queue
* isFull: If queue is full
* IsEmpty: If queue is empty

### Implementation
* Lists
* Modules

#### Implementation of queue Using Lists
* Inserting from Right side of list and removing from left side
     * enqueue: append function
     * dequeue: pop function using 0 index

* Inserting Left side and removing from right side of list
     * enqueue: insert ti zero index
     * dequeue: pop with no ararguments

#### Implementation of queue Using Modules

* dequeue (double ended queue): Collection Module
     * Inserting from Right and removing from left side
          * enqueue: append function
          * dequeue: popleft function
     * Inserting from left and removing from right side
          * enqueue: appendleft function
          * dequeue: pop function

* queue: Queue Module
     * enqueue: put function
     * dequeue: get function

## Priority Queue

They is a modified versoin of the queue data structure in which each element is associated with a priority, and elements are removed according to their priority and if elements have the same priority they are removed according to their position in the queue.

### Setting Priority to values in the queue
* Elements can be assigned to priorities by collecting values in tuples storing the value and its priority
* Value of elements could also signify its priority

### Implementation of Priority Queue
* Lists and Tuples
* Priority Queue class(Queue Module)

## Linked List

Linked List is a dynamic linear Data structure made of chain of nodes in which each node contains a data field and a link or reference to the next node.<br> Sometimes the node contains two links or references, one for the previous node and one for the next. Number of links in each node depends on the type of linked list.<br>
The link or reference on the last node depends on the type of linked list but for most of the types, The last node link value contains the address to the empty value or None.<br>

Nodes of the linked list is stored randomly in memory and not (contegiously) one after the other ike normal lists.

### Terms associated with Linked List

* Node: Each element in the linked list.
* Head or Front: address of First node or Start point of linked list.
* Tail or End: Last Node.
* Data: Data field.

### Advantages
* Dynamic Memory Allocation: No need to specify size.
* Elements are inserted and deleted easily: No need to shift elements, Just change addresses.
* They can be used to implement stacks, queue and graphs.
* Used to represent and manipulate polynomials

### Disadvantages
* Requires more nemory to store addresses
* No elements can be assed randomly, each have to be passed

### Types of Linked Lists
* Singly Linked List: Node contains only one Link.
* Doubly Linked List: Node contains two Links.
* Circular Linked List:

## Singly Linked List

Each Node in the singly linked list contains a data field and a link to the next node, while the last node link field contains a None value.

#### Disadvantages
* Nearly Impossible to move backwards

#### Operations
* Adding Or Insertion: Adding nodes to linked list
* Delete: Removing elements from linked list
* Traversal

### Inserting Elements To Linked List
* Beginning
* End
* Inbetween

#### Steps for inserting to beginning of Linked list
* Create Node
* Copy link from head to new node link field
* Copy address of new node to Head

#### Steps for inserting to end of Linked list
* Create Node
* Set link field of new node to None
* Copy address of new node to last node link address

#### Steps for inserting inbetween Linked list
* Create Node
* Move to Node at one step before desired position for new node
* Change link field of Current node to address of new node
* Set link field of new node of new node no next node after desired position

### Deleting Nodes from Linked List
* Beginning
* End
* Inbetween

#### Steps For deleting nodes from Start of linked list
* Change Head to second Node

#### Steps For deleting nodes from End of linked list
* Change the link field of the second to the last node to None

#### Steps For deleting nodes from middle of linked list
* Move to node one step before before node to be deleted
* Change link field of current node to the address of node after node to be deleted

## Traversing The Linked List
This is going through all nodes in a linked list

## Doubly Linked List

### Insertion Of Nodes

#### Adding nodes at start of linked list
* Create Node
* Set self.head prev reference to new_node
* Change next reference of new_node to self.head

#### Adding nodes at End of linked list
* Create Node
* move to current end of list
* Change the next value of the last node to adress of new node
* Set the previous reference of new_node to address of current last node

#### Adding node to empty linked list
* Create New node
* Set self.head to new node

#### Delete node from start of linked list
* Set self.head to node after self.head
* Set the previous reference of new head to None

#### Delete node from end of linked list
* Move to Second to Last Node in list
* Change current node next reference to None

## Circular Linked Lists
The circular linked list is a linked list where all nodes are connected to form a circle.<br>
In circular linked lists the last node of the linked list contains the address of the first node.<br>
There are tyo types of circular linked lists:
* Circular Singly Linked Lists
* Circular Double linked Lists

### Advantages of Circular Linked lists
* You can start to traverse from any point in the linked list

### Disadvantages Of Circular Linked Lists
* Since it contains no null value, if proper caution is not taken it may lead to an infinite loop

### Operations of circular linked lists
* Insertion: Add nodes
* Deletion : Remove nodes
* Traversal: Loop through all the nodes present in the linked list

#### Insert Node to empty Lined lists
* Create Node
* Set reference of new node points to itself
* set head to new node

#### Insert node at start of linked List
* Create New node 
* Set reference field of the new node to the head
* set reference of last node to the new node

#### Insert node at end of linked List
* Create New node 
* Set reference field of the last node to the new node
* set reference of new node to the head

#### Insert node at middle of linked List
* Create New node 
* Set reference field of the last node to the new node
* set reference of new node to the head


#### Delete Node from Start from Start of Linked List
* Point head to second Node
* Set last node reference field to second node

#### Delete Node from end of linked list
* Traverse to second to last node
* Set Reference to the head

#### Delete node by value
* Traverse to node before the required node
* Set reference to reference next node

### Traverse Circular linked List
* Start from next node of last node
* Print data and go to next node and continue until ref equals head

# Tortise and Hare Algorithm
This is used to find a node n position from the end of a linled list

## Linear and Non-Linear Data Structure
### Linear Structure
* Stack
* Queue
* Linked-Lists

#### Features
* Data items are Traversed Serially and all items are traversed in a single run
* Organised Linearly or sequentially
* Easier to implement
* Only one level depth

### Non-Linear Data Structure
* Trees 
* Graphs

#### Features
* Not Organised Linerly or sequentially

## Trees
A tree is a non-linear data structure that represent relationships between nodes<br>

A tree is a collection of nodes connected by edges and may or may not have children<br>

#### Root:
The top most node of the tree is the root, It is the origin of the tree. There is only one root in a tree<br>

#### Parent Node:
is a node that has a branch to another node<br>
#### Child:
This is a node that was branched from a another node, every node except the roots are child nodes.<br>

#### Siblings:
Nodes that belong to the same parents are sibling nodes<br>

#### Leaf, External or Terminal Nodes:
This are nodes that that have no children.

#### Internal Nodes:
This are nodes with at least one child

#### Path:
The sequence of nodes and edges from one node to another node is known as path

#### Degree of a node
This is the total number of children of the node

#### Degree of a Tree:
The node with the highest degree is the degree of the whole tree

#### Level of the Tree:
This is the amount of generations in the tre

#### Height of Node:
This is the total number of edges that lies on the longest path from any leaf node to a particular node
* Height of tree is the height of the root node

#### Depth
This is the number of edges from root node to partcular node
* Depth of tree is the total edges in longest path from root node to leaf node

### Characterisics of Trees
* The root node can be used to traverse the tree and every non empty tree has a root
* If a tree contains N nodes, The number of edges or links is N-1.
* Every child node can have only one parent but every parent can have multiple children
* Trees are recursive, A tree contains smaller trees called sub-trees

### Types Of trees
* General Tree: There is no limitation for number of children for each node.
* Binary tree: Every node have a maximum of two children.

### Types of Binary trees
* Full Binary tree
* Complete Binary Tree
* Perfect Binary Tree
* Balanced Banary Tree
* pathological Binary Tree

#### Full Binary tree:
This is a type of binary in which a node has exactly zero or two children. They are also called strict Binary Tree.

#### Complete Binary tree
This is a type of binary tree where all levels except last level are completely filled with nodes and all nodes on bottom level are completely filled or filled from left to right.

#### Perfect Binary Tree
This a binary tree where all internal nodes have two children and the leaf nodes are all in same level

#### Balanced Binary Tree
This is a binary tree where hieght of the left and right sub-trees of every node may differ by at most 1

### Binary Search Tree
This a special type of Binary Tree with particular features Listed Below
* The left sub tree of a node contains only nodes with keys lesser than node's key
* The right sub tree of a node contains only nodes with keys greater than node's key
* The left and right sub tree must also be Binary Search Trees

### Applications of Tree Data structure
* Binary Search trees are used for quick search algorihims
* Heap is used for heap sort
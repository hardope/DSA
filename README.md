# Data Structure And Algorithms

## Data structures
### Built in
* Lists
* Tuple
* Dictionary
* Set

### User Defined
* Stack
* Queue
* Linked Lists
* Graphs
* Tree

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



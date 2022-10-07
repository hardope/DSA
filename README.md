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

#### List: Stack can be implemented using lists
* Push operation: list append function
* pop operation: list pop function

#### Modules
 Collections Module(deque class)




# Implementation of queue using List
def enqueue():
     if len(queue) == limit:
          print("Queue Is Fill")
     else:
          element = input("Element: ")
          queue.append(element)

def dequeue():
     if isEmpty():
          print("Queue Is Empty.")
     else:
          print("Removed " + queue.pop(0))

def isEmpty():
     return (len(queue) == 0)

def display():
     print(queue)

queue = list()

limit = int(input("Limit: "))

while True:
     action = input("Action: ")
     if action == "enqueue":
          enqueue()
     elif action == "dequeue":
          dequeue()
     elif action == "exit":
          break
     elif action == "display":
          display()
     else:
          print("Invalid action.", end="\n")

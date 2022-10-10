# Priority Queue Using priority queue class in queue Module

import queue

def enqueue():
     try:
          queue.put_nowait(int(input("Element: ")))
     except:
          print("Queue Is Full")

def dequeue():
     try:
          print(queue.get_nowait())
     except:
          print("Queue is Empty")

limit = int(input("Limit: "))

queue = queue.PriorityQueue(limit)

while True:
     action = input("Action: ")
     print("")
     if action == "enqueue":
          enqueue()
          print("")
     elif action == "dequeue":
          dequeue()
          print("")
     elif action == "exit":
          break
          print("")
     else:
          print("Invalid action.", end="\n")
          print("")
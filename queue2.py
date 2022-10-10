# Implementation of queue using Priority queue class from queue Module

import queue

def enqueue():
     try:
          element = input("Element: ")
          queue.put_nowait(element)
     except:
          print("Queue is Full.")

def dequeue():
     try:
          print(queue.get_nowait())
     except:
          print("Queue Is Empty.")

def isEmpty():
     return (len(queue) == 0)

limit = int(input("Limit: "))
queue = queue.Queue(limit)
while True:
     action = input("Action: ")
     if action == "enqueue":
          enqueue()
     elif action == "dequeue":
          dequeue()
     elif action == "exit":
          break
     else:
          print("Invalid action.", end="\n")
# Priority Queue Using Lists and Tuples

def enqueue():
     if len(queue) == limit:
          print("Queue Is Full.")
     else:
          value = input("Input Value: ")
          priority = int(input("Input Priority: "))
          queue.append((priority, value))
          queue.sort()

def dequeue():
     if len(queue) == 0:
          print("Queue Is Empty.")

     else:
          print("Removed ", queue.pop())

queue = []

limit = int(input("Limit: "))

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
     elif action == "display":
          print(queue)
          print("")
     else:
          print("Invalid action.", end="\n")
          print("")
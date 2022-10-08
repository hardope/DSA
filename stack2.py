import queue

# implementation of stack using queue Module

# push function
def push():
     if stack.full():
          print("Stack is full.")
     else:
          element = input("Enter Eement: ")
          stack.put(element)
          

# pop function
def pop():
     if stack.empty():
          print("Stack is Empty.")
     else:
          e = stack.get()
          print(f"Removed {e}", end="\n")
          print(list(stack.queue))


limits = 2000
limits = int(input("Set Limit: "))
stack = queue.LifoQueue(limits)
while True:
     action = input("Action: ")
     if action == "pop":
          pop()
     elif action == "push":
          push()
     elif action == "exit":
          break
     else:
          print("Invalid action.", end="\n")
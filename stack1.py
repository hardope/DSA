import collections
# implementation of stack using collection

# push function
def push():
     if len(stack) >= limits:
          print("Stack Is Full.",end="\n")
     else:
          element = input("Enter Eement: ")
          stack.append(element)
          print(stack, end="\n")

# pop function
def pop():
     if isEmpty(stack):
          print("Stack Empty", end="\n")
     else:
          e = stack.pop()
          print(f"Removed {e}", end="\n")
          print(stack, end="\n")

# is empty function
def isEmpty(stack):
     if len(stack) < 1:
          return True
     else:
          return False
# peek function
def peek(stack):
     print(stack[-1])

limits = 2000
stack = collections.deque()
limits = int(input("Set Limit: "))
while True:
     action = input("Action: ")
     if action == "pop":
          pop()
     elif action == "push":
          push()
     elif action == "peek":
          peek(stack)
     elif action == "exit":
          break
     else:
          print("Invalid action.", end="\n")

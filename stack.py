limits = 2000
stack = []
def push():
     if len(stack) >= limits:
          print("Stack Is Full.",end="\n")
     else:
          element = input("Enter Eement: ")
          stack.append(element)
          print(stack, end="\n")

def pop():
     if not stack:
          print("Stack Empty", end="\n")
     else:
          e = stack.pop()
          print(f"Removed {e}", end="\n")
          print(stack, end="\n")

limits = int(input("Set Limit: "))
while True:
     action = input("Action: ")
     if action == "pop":
          pop()
     elif action == "push":
          push()
     elif action == "limit":
          limit()
     else:
          print("Invalid action.", end="\n")
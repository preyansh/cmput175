class Stack:
  def __init__(self):
    self.items = []
  
  def isEmpty(self):
    return self.items == []
  
  def push(self, item):
    self.items.append(item)
  
  def pop(self):
    return self.items.pop()
  
  def peek(self):
    return self.items[len(self.items)-1]
  
  def size(self):
    return len(self.items)
  
def function_to_analyze(my_list):
  stack = Stack()
  for item in my_list:
    stack.push(item)
  new_list = []
  while not stack.isEmpty():
    new_list.append(stack.pop())
  return new_list

#Function: given my_list, the functioniterates over that list, for item in the 
#list the item is pushed onto the stack object, a new, empty list, is created 
#and while the first stack is not empty, each item on the top of the stack is 
#popped onto the new_list, which is then returned. Basically the function 
#reverses the elements in my_list.
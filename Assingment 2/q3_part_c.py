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
  
def function_to_analyze(string):
  stack = Stack()
  for char in string:
    stack.push(char)
  another_stack = Stack()
  while stack.size() > another_stack.size():
    another_stack.push(stack.pop())
  if not stack.size() == another_stack.size():
    another_stack.pop()
  while not stack.isEmpty():
    if not stack.pop() == another_stack.pop():
      return False
  return True

class Stack:
  def __init__(self):
    self.items = []

  def isEmpty(self):
    return self.items == []
    
  def push(self, item):
    self.items.insert(0,item)
      
  def pop(self):
    return self.items.pop(0)
      
  def peek(self):
    return self.items[0]
      
  def size(self):
    return len(self.items)
   
open_parens = ['{', '[', '(']   
pairs = {')':'(', ']':'[', '}':'{'}

def function_to_analyze(input_string):
  stack = Stack()
  for char in input_string:
    if char in open_parens:
      stack.push(char)
    elif char in pairs:
      if stack.isEmpty():
        return False
      if not stack.peek() == pairs[char]:
        return False
      stack.pop()
  return stack.isEmpty()
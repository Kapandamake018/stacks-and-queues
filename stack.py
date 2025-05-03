class Stack:
  def __init__(self):
    self.stack = []
    
  def push(self, value):
    return self.stack.append(value)
  
  def pop(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.stack.pop()
  
  def peek(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.stack[-1]

  def isEmpty(self):
    return len(self.stack) == 0
  
  def size(self):
    return len(self.stack)
  

stack = Stack()

stack.push(10)
stack.push(1)
stack.push(29)
stack.push(5)
stack.push(13)
print("push:", stack.stack)
print("pop:",stack.pop())
print("pop:",stack.pop())
print("peek:",stack.peek())
print("isEmpty:",stack.isEmpty())
print("size:",stack.size())

from collections import deque

class Queue:
  def __init__(self):
    self.queue = deque()
    
  def enqueue(self, value):
    return self.queue.append(value)
  
  def dequeue(self):
    if self.isEmpty():
      return "Queue is empty"
    return self.queue.popleft()
  
  def peek(self):
    if self.isEmpty():
      return "Queue is empty"
    return self.queue[0]
  
  def isEmpty(self):
    return len(self.queue) == 0
  
  def size(self):
    return len(self.queue)
  
  

queue = Queue()

queue.enqueue(10)
queue.enqueue(5)
queue.enqueue(29)
queue.enqueue(88)
queue.enqueue(7)
print("enqueue:",queue.queue)
print("dequeue:",queue.dequeue())
print("dequeue:",queue.dequeue())
print("queue:",queue.queue)
print("peek:",queue.peek())
print("isEmpty:",queue.isEmpty())
print("size:",queue.size())


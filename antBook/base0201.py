import queue
import numpy as np

def fact(n):
  if n == 0:
    return 1
  return n * fact(n-1)

def fib_v0(n):
  if n == 0 or n == 1:
    return n
  return fib(n-1) + fib(n-2)

class fibonacci:
  def __init__(self, max_n):
    self.memo = np.ones(max_n)*(-1)

  def fib(self, n):
    if n == 0 or n ==1:
      return n
    if self.memo[n] > 0:
      return self.memo[n]
    self.memo[n] = self.fib(n-1) + self.fib(n-2)
    return self.memo[n]

def test_liststack():
  stack = []
  stack.append(1)
  stack.append(10)
  stack.append(13)
  print(stack)
  print(stack.pop())
  print(stack.pop())
  print(stack)

def test_queue():
  q = queue.Queue()
  q.put(12)
  q.put(14)
  q.put(20)
  print(q.qsize())
  print(q.get())
  print(q.get())
  print(q.empty())
  print(q.qsize())

def test_fibonacci():
  f = fibonacci(100)
  print(10, f.fib(10))
  print(40, f.fib(40))

if __name__ == '__main__':
  test_queue()


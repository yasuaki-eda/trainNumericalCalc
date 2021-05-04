'''
 2-1. 全探索 部分和
'''

class partial_sum:
  def __init__(self, a, k):
    self.N = len(a)
    self.a = a
    self.k = k
    self.result = []

  def dfs(self, x, sum):
    if x == self.N:
      return sum == self.k
    if self.dfs(x+1, sum + self.a[x]) :
      self.result.append(self.a[x])
      return True
    if self.dfs(x+1, sum):
      return True
    return False


  def solve(self):
    if self.dfs(0, 0) :
      print('Yes.', self.result)
    else:
      print('No.')

if __name__ == '__main__':
  a = [1, 2, 4, 7]
  k = 13
  p = partial_sum(a, k)
  p.solve()



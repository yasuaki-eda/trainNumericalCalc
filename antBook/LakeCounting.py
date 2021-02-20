import numpy as np



def init_lake():
  # N, M = 10, 12
  lake = np.array([
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0]
  ])
  return lake

class LakeCount:
  WHITE = 0
  BLACK = 1

  def __init__(self, lake):
    self.lake = lake
    self.N, self.M = lake.shape
    self.state = np.ones((self.N, self.M)) * LakeCount.WHITE # all white
    self.lake_count = 0

  def solve(self):
    for y in range(self.N):
      for x in range(self.M):
        if (self.state[y, x] == LakeCount.WHITE) & (self.lake[y, x] == 1):
          self.DFS(x, y)
          self.lake_count += 1

  def DFS(self, x, y):
    self.state[y, x] = LakeCount.BLACK
    # 8近傍を探索
    for i in range(-1, 2):
      for j in range(-1, 2):
        nx = x + j
        ny = y + i
        if (0 <= nx) & (nx<self.M) & (0<=ny) & (ny<self.N):
          if (self.state[ny, nx] == LakeCount.WHITE) & (self.lake[ny, nx] == 1):
            self.DFS(nx, ny)

def test_LakeCount():
  lc = LakeCount(init_lake())
  lc.solve()
  print(lc.lake_count)
  print(lc.state)


if __name__ == '__main__':
  test_LakeCount()

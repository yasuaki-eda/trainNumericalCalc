import numpy as np
import queue

WALL = 1
ROAD = 0
START = 2
END = 3
WHITE = 0
GRAY = 1
BLACK = 2

class MazeBFS:
  def __init__(self, maze):
    self.maze = maze
    self.H, self.W = maze.shape
    self.start = np.argwhere(maze==START)[0]
    self.end = np.argwhere(maze==END)[0]
    self.answer = -1
  
  def solve(self):
    q = queue.Queue()
    m1 = np.ones((self.H, self.W), dtype='int16') * WHITE  # 探索した道をblack
    d = np.zeros((self.H, self.W), dtype='int16')          # startからの距離をセット
    pi = np.zeros((self.H, self.W, 2), dtype='int16')      # 直前の位置をセット
    m1 = np.where(self.maze == WALL, BLACK, m1)

    distance = 0
    d[self.start[0], self.start[1]] = distance
    pi[self.start[0], self.start[1], :] = -1
    m1[self.start[0], self.start[1]] = GRAY
    q.put(self.start)
   
    while not q.empty():
      t = q.get()
      x, y = t[0], t[1]

      # 周辺を探す
      for dxy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        dx = x + dxy[0]
        dy = y + dxy[1]
        if (0 <= dx) & ( dx < self.H ) & ( 0 <= dy) & ( dy < self.W):
          if m1[dx, dy] == WHITE:
            pi[dx, dy, 0], pi[dx, dy, 1] = dx, dy 
            q.put([dx, dy])
            distance = d[x, y] + 1
            d[dx, dy] = distance
            m1[dx, dy] = GRAY
      m1[x, y] = BLACK
    
    self.result = d[self.end[0], self.end[1]]
    print('answer:', int(self.result))

    return m1, d, pi


def init_maze():
  maze = np.array([
    [1, 2, 1, 1, 1, 1, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [0, 1, 0, 1, 1, 0, 1, 1, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 3, 1]
  ])
  return maze


if __name__ == '__main__':
  maze = init_maze()
  mb = MazeBFS(maze)
  m1, d, pi = mb.solve()
  print(m1)
  print(d)
  print(pi[:,:,0])
  print(pi[:,:,1])



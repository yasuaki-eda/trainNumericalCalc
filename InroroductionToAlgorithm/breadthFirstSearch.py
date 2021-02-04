import numpy as np 
import queue

def init_graph():
  G = {
    0: [1, 4],
    1: [0, 5],
    2: [3, 5, 6],
    3: [2, 6, 7],
    4: [0],
    5: [1, 2, 6],
    6: [2, 3, 5, 7],
    7: [3, 6]
  }
  return G

def BFS(G, s):
  size = len(G)
  q = queue.Queue()
  WHITE, GRAY, BLACK = 0, 1, 2
  color = np.ones(size) * WHITE
  d = np.ones(size) * 2e32
  pi = np.ones(size) *(-1)
  color[s] = GRAY
  d[s] = 0
  G_list = list(G.items())
  q.put(G_list[s])
  while not q.empty():
    u = q.get()
    for v in u[1]:
      if color[v] == WHITE:
        color[v] = GRAY
        d[v] = d[u[0]] + 1
        pi[v] = u[0]
        q.put(G_list[v])
    color[u[0]] == BLACK
  return d, pi


if __name__ == '__main__':
  G = init_graph()
  d, pi = BFS(G, 1)
  print('G', G)
  print('d', d)
  print('pi', pi)



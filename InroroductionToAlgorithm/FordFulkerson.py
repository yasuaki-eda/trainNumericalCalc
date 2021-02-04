import numpy as np
import breadthFirstSearch as BFS
import copy


def init_graph():
  G = {
    0: [1, 2],
    1: [2, 3],
    2: [1, 4],
    3: [2, 5],
    4: [3, 5],
    5: []
  }
  C = {
    0: [16, 13],
    1: [10, 12],
    2: [ 4, 14],
    3: [ 9, 20],
    4: [ 7,  4],
    5: []
  }
  return G, C

def MaxFlow(G0, C0):
  C = copy.deepcopy(C0)
  G = copy.deepcopy(G0)
  s = 0
  t = len(G) - 1
  iterator = 0
  while iterator < 10000:  # while Trueでいいはず
#    print('iterator:', iterator)
    iterator += 1

    d, pi = BFS.BFS(G, s)
    if d[t] > len(G)+1:
      break

    route = []
    route.append(t)
    x = int(pi[t])
    while x >= 0 :
      route.append(x)
      x = int(pi[x])
    route.reverse()
#    print (route)  # s→tのパス

    # パスに沿ったcostのminを調べる
    min_cost = 2**16
    for x in range(len(route)-1):
      cidx = G[route[x]].index(route[x+1])
      c = C[route[x]][cidx]
      if c < min_cost:
        min_cost = c
#    print('min cost:', min_cost)

    # Cを更新
    for x in range(len(route)-1):
      cidx = G[route[x]].index(route[x+1])
      C[route[x]][cidx] -= min_cost
      if C[route[x]][cidx] == 0:
        # Gから削除
        del G[route[x]][cidx]

#    print('Cf', C)
#    print('Gf', G)

#  print('C', C0)
#  print('Gf', G)
#  print('Cf', C)
  F = copy.deepcopy(C0)
  for x in range(len(C)):
    for y in range(len(C[x])):
      F[x][y] = C0[x][y] - C[x][y]
#  print('Frow', F)
#  print('G', G0)
  return F





if __name__ == '__main__':
  G0, C0 = init_graph()
  F = MaxFlow(G0, C0)
  print('G', G0)
  print('C', C0)
  print('Flow', F)



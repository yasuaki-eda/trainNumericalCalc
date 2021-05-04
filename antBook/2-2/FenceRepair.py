import numpy as np

'''
 p49 POJ3253
 Fence Repair
'''

'''
 最小コスト=34
'''
def init_fence():
  N = 3
  bord = [8, 5, 8]
  return N, bord

'''
 最小コスト=33
'''
def init_fence2():
  N = 5
  bord = [1, 3, 2, 4, 5]
  return N, bord

'''
 失敗作品 (fence2は最小コスト=33)
'''
def fence_repair_v0():
  N, bord = init_fence2()
  length = sum(bord)
  cost = 0
  bord.sort(reverse=True)
  for n in range(N-1):
    cost += sum(bord)
    b = bord.pop(0)

  print('length:%d, cost:%d' %(length, cost))
  return cost

def fence_repair():
  N, bord = init_fence2()
  length = sum(bord)
  cost = 0
  bord.sort()
  while(len(bord) > 1):
    print('bord:' + str(bord)+ ' cost:' + str(cost))
    bord, cost = cut(bord, cost)
  print('bord:' + str(bord)+ ' cost:' + str(cost))
  return cost

def cut(bord, cost):
  bord.sort()
  b = bord.pop(0)+bord.pop(0)
  bord.append(b)
  cost += b
  return bord, cost


if __name__ == '__main__':
  fence_repair()




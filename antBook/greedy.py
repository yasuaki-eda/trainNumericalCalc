import numpy as np


'''
 2-2 : 貪欲法
'''

def coin_greedy(pay=620):
  coins = init_coin()
  print(coins)
  amount = 0
  coin_num = 0
  for c in coins:
    for i in range(c[1]):
      if amount + c[0] <= pay:
        amount += c[0]
        coin_num += 1
        print('coin:' + str(c[0]) + ' amount:' + str(amount))
  
  print(amount, coin_num)
  return amount, coin_num

def init_coin():
  coins = {
    1:3, 
    5:2,
    10: 1,
    50:3,
    100:0,
    500:2
  }

  # keyでsort 
  coins1 = sorted(coins.items(), reverse=True)
  return coins1

'''
 先にソートしたほうが早いはず
'''
def schedule_greedy():
  N, s, t = init_schedule()
  task_count = 0
  time = 0
  while True:
    end_time = t[N-1] + 1
    tmp_n = -1
    for n in range(N):
      if time < s[n]:
        if t[n] < end_time:
          end_time = t[n]
          tmp_n = n
    
    if tmp_n != -1:
      time = end_time
      task_count += 1
      print('start:' + str(s[tmp_n]) + ' end:' + str(t[tmp_n]))
    else :
      break
  print(task_count)
  return task_count


def init_schedule():
  n = 5
  s = [1, 2, 4, 6, 8]
  t = [3, 5, 7, 9, 10]
  return n, s, t

if __name__ == '__main__':
#  coin_greedy()
  schedule_greedy()




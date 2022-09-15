import sys
import collections
input = sys.stdin.readline

N, M = map(int, input().split())
chicken = []
house = []
ans = []
graph = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
  for j in range(N):
    if graph[i][j] == 2:
      chicken.append((i, j))
    elif graph[i][j] == 1:
      house.append([(i, j), 65]) # 치킨 거리 최댓값 설정

def getDist(r1, c1, r2, c2):
  return (abs(r1-r2) + abs(c1-c2))

def combination(arr, n):
  ret = []

  if n == 0:
    return [[]]
  
  for i in range(len(arr)):
    elem = arr[i]
    rest_arr = arr[i+1:]
    for C in combination(rest_arr, n-1):
      ret.append([elem] + C)
  
  return ret

for comb in combination(chicken, M):
  tmp = 0
  for pos_chicken in comb:
    for pos_house in house:
      pos_house[1] = min(pos_house[1], getDist(pos_house[0][0], pos_house[0][1], pos_chicken[0], pos_chicken[1]))
  
  for pos_house in house:
    tmp += pos_house[1]
    pos_house[1] = 65 # backtracking
  ans.append(tmp)



print(min(ans))

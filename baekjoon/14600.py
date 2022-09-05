import sys
import collections
input = sys.stdin.readline

K = int(input())
SIZE = 2**K
wx, wy = map(int, input().split())
wx = SIZE - wy + 1
wy = wx
cnt = 1
floor = [[0]*(SIZE+1) for _ in range(SIZE+1)]
floor[wx][wy] = -1

def hasWater(x, y):
  if floor[x][y] == -1 or floor[x+1][y] == -1 or floor[x+1][y+1] == -1 or floor[x][y+1] == -1:
    return True
  
  return False

def dnq(x, y, cnt, curSize, area):
  if curSize <= 2:



dnq(0, 0, 0, SIZE, 0)
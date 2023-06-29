import sys
import collections

input = sys.stdin.readline

N = int(input())
prices = list(map(int, input().split()))
cur_max = prices[-1]
total = 0

for i in range(N-2, -1, -1):
    if cur_max < prices[i]:
        cur_max = prices[i]
    else:
        total += cur_max - prices[i]

print(total)
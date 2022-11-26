import sys
import collections
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

def backtracking(idx, sum):
    global cnt
    if idx >= N:
        return
    sum += arr[idx]
    if sum == S:
        cnt += 1
    
    backtracking(idx+1, sum - arr[idx])
    backtracking(idx+1, sum)

cnt = 0
backtracking(0, 0)
print(cnt)

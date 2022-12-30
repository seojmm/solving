import sys
import collections
input = sys.stdin.readline

N, M = map(int, input().split())
title = []
max_val = [-1]
for _ in range(N):
    a, b = input().split()
    title.append(a)
    max_val.append(int(b))


def bisect_left(arr, target):
    l, r = 0, len(arr)-1

    while l < r:
        mid = (r-l)//2 + l

        if arr[mid] < target:
            l = mid + 1
        else:
            r = mid

    return r


for _ in range(M):
    cur = int(input())
    cur_idx = bisect_left(max_val, cur)
    print(title[cur_idx-1])

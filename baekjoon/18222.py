import sys
import collections
input = sys.stdin.readline

k = int(input())

def solve(n):
    if n == 0: return 0
    if n == 1: return 1
    if n%2 == 1:
        return 1 - solve(n//2)
    else:
        return solve(n//2)

print(solve(k-1))
import sys
import collections
import itertools
input = sys.stdin.readline

n = 4
C = [0]*(n+1)
C[0] = 1
C[1] = 1
C[2] = 2
for i in range(3, n+1):
    C[i] = 0
    for j in range(i):
        C[i] += C[j]*C[i-1-j]

print(C)
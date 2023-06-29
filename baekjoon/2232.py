import sys

input = sys.stdin.readline

N = int(input())
P = [0]
for _ in range(N): P.append(int(input()))
P.append(0)

result = []

for i in range(1, N+1):
    if P[i-1] <= P[i] and P[i] >= P[i+1]:
        result.append(i)

for r in result:
    print(r)
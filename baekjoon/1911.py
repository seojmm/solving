import sys

input = sys.stdin.readline

N, L = map(int, input().split())

pos = []
for i in range(N):
    pos.append(list(map(int, input().split())))

pos.sort(key=lambda x: x[0])

ans = 0
cur = 0

for p in pos:
    if cur > p[0]:
        p[0] = cur

    while p[0] < p[1]:
        p[0] += L
        ans += 1

    cur = p[0]

print(ans)
import collections

dq = collections.deque()

N = int(input())

for i in range(1, N+1, 1):
    dq.append(i)

while (len(dq) > 1):
    dq.popleft()
    dq.append(dq.popleft())
print(dq[0])

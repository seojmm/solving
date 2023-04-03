import sys
import collections
input = sys.stdin.readline

visited = [[False]*1001 for _ in range(1001)]
S = int(input())

q = collections.deque()
q.append((1, 0, 0))
visited[1][0] = True
while q:
    x, time, clip = q.popleft()

    if x == S:
        print(time)
        break

    new_x, new_clip = 0, 0
    for i in range(3):
        if i == 0:
            new_x, new_clip = x + clip, clip
        elif i == 1:
            new_x, new_clip = x, x
        else:
            new_x, new_clip = x - 1, clip
        if 1 <= new_x <= 1000 and new_clip >= 0 and not visited[new_x][new_clip]:
            q.append((new_x, time+1, new_clip))
            visited[new_x][new_clip] = True

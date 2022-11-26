import sys
import collections
input = sys.stdin.readline

R, C = map(int, input().split())
graph = []
ansS, ansW = 0, 0
for i in range(R):
    tmp = list(input().rstrip())
    for j in range(C):
        if tmp[j] == "o": ansS += 1
        elif tmp[j] == "v": ansW += 1
    graph.append(tmp)
visited = [[False]*C for _ in range(R)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    global ansS, ansW
    sheep, wolves = 0, 0
    q = collections.deque()
    
    q.append((x, y))
    visited[x][y] = True

    if graph[x][y] == "o": sheep += 1
    elif graph[x][y] == "v": wolves += 1
    while q:
        curX, curY = q.popleft()
        for k in range(4):  
            nx, ny = curX + dx[k], curY + dy[k]
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            if visited[nx][ny] or graph[nx][ny] == "#":
                continue
            if graph[nx][ny] == "v":
                wolves += 1
            if graph[nx][ny] == "o":
                sheep += 1

            q.append((nx, ny))
            visited[nx][ny] = True
    
    if sheep and wolves:
        if sheep > wolves: ansW -= wolves
        else: ansS -= sheep



for i in range(R):
    for j in range(C):
        if (graph[i][j] == "v" or graph[i][j] == "o") and not visited[i][j]:
            visited[i][j] = True
            bfs(i, j)
            

print(ansS, ansW)


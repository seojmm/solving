import sys
import collections
input = sys.stdin.readline

N, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for day in range(2001):
    visited = [[0]*N for _ in range(N)]
    flag = False
    for i in range(N):
        for j in range(N):
            if visited[i][j]: continue
            q = collections.deque()
            tmp = []
            q.append((i, j))
            tmp.append((i, j))
            visited[i][j] = 1

            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    
                    if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
                    if visited[nx][ny]: continue
                    if L <= abs(graph[x][y] - graph[nx][ny]) <= R:
                        visited[nx][ny] = 1
                        q.append((nx, ny))
                        tmp.append((nx, ny))
                        flag = True

            people = 0
            for x, y in tmp:
                people += graph[x][y]
            people //= len(tmp)
            for x, y in tmp:
                graph[x][y] = people
    

    if not flag:
        print(day)
        break
  

    



        
    
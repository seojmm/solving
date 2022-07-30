import sys
import collections
input = sys.stdin.readline

N, pE, pW, pS, pN = list(map(int, input().split()))
prob = [pE, pW, pS, pN]
visited = [[0]*30 for _ in range(30)]
dx = [0, 0, 1, -1] # 동서남북
dy = [1, -1, 0, 0] # 역시 동서남북
ans = 0
vNum = 0

def dfs(x, y, cnt, total):
    global ans

    if cnt == N:
        ans += total
        return

    if visited[x][y]:
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if visited[nx][ny]: return
        if nx < 1 or nx > 2*(N+1)-1 or ny < 1 or ny > 2*(N+1)-1: return

        visited[nx][ny] = 1
        dfs(nx, ny, cnt + 1, total*prob[i])
        visited[nx][ny] = 0

visited[N][N] = 1
dfs(N, N, 0, 1)
print(ans*0.01)
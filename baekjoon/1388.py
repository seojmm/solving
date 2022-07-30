import sys
input = sys.stdin.readline

N, M = map(int, input().split())
floor = []
visited = [[False]*M for _ in range(N)]
ans = 0

def dfs(x, y, type):
    if visited[x][y] == True:
        return
    
    visited[x][y] = True

    if type == 0:
        if y == M-1: return
        if floor[x][y+1] != "-":
            return
        dfs(x, y+1, 0)
    else:
        if x == N-1: return
        if floor[x+1][y] != "|": return
        dfs(x+1, y, 1)

for i in range(N):
    floor.append(input().rstrip())

for i in range(N):
    for j in range(M):
        if visited[i][j] == False:
            if floor[i][j] == "-":
                dfs(i, j, 0)
                ans += 1
                #print(i, j, 0)
            else:
                dfs(i, j, 1)
                ans += 1
                #print(i, j, 1)

print(ans)
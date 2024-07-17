import sys, collections
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ans = 0

h, w = map(int, input().split())


board = []
for _ in range(h):
    board.append(list(map(int, input().strip().split())))

def is_all_zero(board):
    max_val = -1
    for row in board:
        max_val = max(max_val, max(row))

    return max_val == 0

def bfs(x, y, board):
    
    q = collections.deque()
    q.append((x, y))
    visited[x][y] = 1

    while len(q) > 0:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < h and 0 <= ny < w and visited[nx][ny] == 0 and board[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = 1

    return visited

flag = True
tmp = 0

while flag:
    visited = [[0]*w for _ in range(h)]
    bfs(ans, ans, board)

    for i in range(h):
        for j in range(w):
            if visited[i][j] == 1:
                for k in range(4):
                    ni, nj = i + dx[k], j + dy[k]
                    if 0 <= ni < h and 0 <= nj < w and board[ni][nj] == 1:
                        board[ni][nj] = 0
                        tmp += 1


    if is_all_zero(board):
        break
        
    ans += 1
    tmp = 0

print(ans+1)
print(tmp)
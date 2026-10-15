N, L = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))


def find(path):
    visited = [0]*N
    for i in range(1, N):
        if abs(path[i] - path[i-1]) > 1:
            return False
        
        if path[i-1] > path[i]:
            for j in range(L):
                if i+j >= N or path[i] != path[i+j] or visited[i+j]:
                    return False
                if path[i] == path[i+j]:
                    visited[i+j] = True
        elif path[i-1] < path[i]:
            for j in range(L):
                if i-j <= 0 or path[i-1] != path[i-j-1] or visited[i-j-1]:
                    return False
                if path[i-1] == path[i-j-1]:
                    visited[i-j-1] = True
    
    return True


answer = 0
cross = list(zip(*board))

for i in range(N):
    if find(board[i]):
        answer += 1
    if find(cross[i]):
        answer += 1

print(answer)
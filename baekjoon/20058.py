import sys
import collections
input = sys.stdin.readline

N, Q = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(2**N)]
steps = list(map(int, input().split()))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def rotate(size):
    ret = [[0]*(2**N) for _ in range(2**N)]
    for x in range(0, 2**N, size):
        for y in range(0, 2**N, size):
            for i in range(size):
                for j in range(size):
                    ret[x+j][y+size-1-i] = graph[x+i][y+j]

    return ret


def melt():
    list_melt = []
    for x in range(2**N):
        for y in range(2**N):
            cnt = 0
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx >= 2**N or ny < 0 or ny >= 2**N:
                    continue
                if graph[nx][ny] > 0:
                    cnt += 1

            if cnt < 3 and graph[x][y] > 0:
                list_melt.append((x, y))

    for x, y in list_melt:
        graph[x][y] -= 1


def printAnswer():
    total = 0
    cnt_max = 0
    visited = [[False]*(2**N) for _ in range(2**N)]
    for x in range(2**N):
        for y in range(2**N):
            cnt = 0
            if visited[x][y] or graph[x][y] == 0:
                continue
            q = collections.deque()
            q.append((x, y))
            visited[x][y] = True

            while q:
                curX, curY = q.popleft()
                total += graph[curX][curY]
                cnt += 1

                for i in range(4):
                    nx, ny = curX + dx[i], curY + dy[i]
                    if nx < 0 or nx >= 2**N or ny < 0 or ny >= 2**N:
                        continue
                    if graph[nx][ny] > 0 and not visited[nx][ny]:
                        q.append((nx, ny))
                        visited[nx][ny] = True

            cnt_max = max(cnt_max, cnt)

    print(total)
    print(cnt_max)


for L in steps:
    size = 2**L
    graph = rotate(size)
    melt()

printAnswer()

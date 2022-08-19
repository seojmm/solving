import sys
import collections
input = sys.stdin.readline


N, M, H = map(int, input().split())
if M == 0:
    print(0)
    sys.exit(0)
ladder = [[False]*N for _ in range(H)]

for _ in range(M):
    a, b = map(int, input().split())
    ladder[a-1][b-1] = True


def move():
    for start in range(N):
        k = start
        for i in range(H):
            if ladder[i][k]:  # 오른쪽으로 이동
                k += 1
            elif k > 0 and ladder[i][k-1]:  # 왼쪽으로 이동
                k -= 1

        if k != start:
            return False

    return True


def dfs(x, y, cnt):
    global ans
    if move():
        ans = min(ans, cnt)
        return
    elif cnt == 3 or ans <= cnt:
        return

    for i in range(x, H):  # 가로선
        k = y if i == x else 0
        for j in range(k, N-1):  # 세로선
            if not ladder[i][j] and not ladder[i][j+1]:
                ladder[i][j] = True
                dfs(i, j+2, cnt+1)
                ladder[i][j] = False


ans = 4
dfs(0, 0, 0)
print(ans if ans < 4 else -1)

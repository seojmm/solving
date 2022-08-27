import sys
import collections
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, D = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def shoot(y, position, tmpBoard):
    for d in range(1, D+1):
        for left in range(d, -1, -1):
            height = d - left
            if height > 0 and 0 <= y-height < N and 0 <= position - left < M and tmpBoard[y-height][position-left] == 1:
                return (y-height, position-left)
        for right in range(1, d+1, 1):
            height = d - right
            if height > 0 and 0 <= y-height < N and 0 <= position + right < M and tmpBoard[y-height][position+right] == 1:
                return (y-height, position+right)

    return None

def simulation(positions):
    tmpBoard = [line[:] for line in board]
    killedNum = 0

    for y in range(N, 0, -1):
        killedArr = []
        for position in positions:
            killedEnemy = shoot(y, position, tmpBoard)
            if killedEnemy:
                killedArr.append(killedEnemy)
        for killedEnemy in killedArr:
            if tmpBoard[killedEnemy[0]][killedEnemy[1]] == 1:
                tmpBoard[killedEnemy[0]][killedEnemy[1]] = 0
                killedNum += 1
    
    return killedNum


ans = 0
for i in range(M):
    for j in range(i+1, M):
        for k in range(j+1, M):
            ans = max(ans, simulation((i, j, k)))

print(ans)

import sys
import collections
import itertools
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# 모든 경우의 수 구하기
p = list(itertools.permutations(range(1, 9), 8))
ans = 0
for order in p:
    order = list(order)
    order = order[:3] + [0] + order[3:]
    score = 0
    curHitter = -1
    for inning in board:
        outcounts = 0
        base1, base2, base3 = 0, 0, 0
        while outcounts < 3:
            curHitter = (curHitter + 1)%9
            if inning[order[curHitter]] == 0:
                outcounts += 1
            elif inning[order[curHitter]] == 1:
                score += base3
                base1, base2, base3 = 1, base1, base2
            elif inning[order[curHitter]] == 2:
                score += base2 + base3
                base1, base2, base3 = 0, 1, base1
            elif inning[order[curHitter]] == 3:
                score += base1 + base2 + base3
                base1, base2, base3 = 0, 0, 1
            else:
                score += base1 + base2 + base3 + 1
                base1, base2, base3 = 0, 0, 0

    ans = max(ans, score)

print(ans)

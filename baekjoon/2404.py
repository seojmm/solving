import sys
input = sys.stdin.readline

p, q, a, n = map(int, input().split())
visited = [0 for _ in range(801)]

ans = 0

def check(p, q, history: list):
    under = 1
    upper = 0
    for e in history:
        under *= e
        upper += e*under

    cand = sum(history)/tmp

    if p/q == cand:
        return True

    return False

def backtracking(depth, history, n):
    if len(history) == n and check(p, q, history):
        ans += 1
        return
    
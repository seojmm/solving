import sys
import math

input = sys.stdin.readline

# def getDist(x1, y1, x2, y2):
#     return math.sqrt((x2-x1)**2 + (y2-y1)**2)


def getPytha(x, y):
    return x*x + y*y


N = int(input())

N //= 2
x = 0
y = N-1
ans = 0

while (y >= 0):
    d = getPytha(x+1, y)
    if (d <= N*N):
        x += 1
    if (d >= N*N):
        y -= 1
    ans += 1

print(ans*4)

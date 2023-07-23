import sys
import collections

input = sys.stdin.readline

while True:
    digit = [0]*10
    A, B = map(int, input().split())
    if A == 0 and B == 0: break

    while A <= B:
        ss = str(A)

        for ch in ss:
            digit[int(ch)] += 1
        A += 1

    print(" ".join(map(str, digit)))
            
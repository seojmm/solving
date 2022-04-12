import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    s = list(input().rstrip())

    l, r = 0, n-1
    minVal = n
    while l < r:
        if s[l] == "a" and s[r] == "a":
            substr = s[l:r+1]
            if substr.count("a") > substr.count("b") and substr.count("a") > substr.count("c"):
                minVal = 
import sys

input = sys.stdin.readline

T = int(input())

while (T):
    m, n = map(int, input().split())
    r, c = 0, 1

    print(1)

    while (r < m):
        print(f"({r},{c})")
        if r % 2 == 0:
            c += 1
        else:
            c -= 1

        if c == n or c == 0:
            if r % 2 == 0:
                c -= 1
            else:
                c += 1

            r += 1

    for i in range(m-1, -1, -1):
        print(f"({i},0)")

    T -= 1

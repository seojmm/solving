import sys

input = sys.stdin.readline

if __name__ == '__main__':
    X = int(input())
    s_list = [64, 32, 16, 8, 4, 2, 1]

    cnt = 0

    for s in s_list:
        if X >= s:
            cnt += 1
            X -= s

        if X == 0:
            break

    print(cnt)



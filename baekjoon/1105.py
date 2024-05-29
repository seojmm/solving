import sys

input = sys.stdin.readline

if __name__ == '__main__':
    l, r = input().strip().split()
    cnt = 0

    if l == r:
        cnt = r.count('8')
    else:
        if len(l) == len(r) and l[0] == r[0]:
            for i in range(len(l)):
                if l[i] == r[i]:
                    if l[i] == '8':
                        cnt += 1
                else:
                    break

    print(cnt)


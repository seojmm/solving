import sys
input = sys.stdin.readline

if __name__ == '__main__':

    T = int(input())
    for _ in range(T):
        p = input().strip()
        n = int(input())
        AC = input().strip()
        res = "error"

        if n > 0:
            isEmpty = False
            isError = False
            AC = AC[1:-1].split(',')

            l, h = 0, n-1

            for command in p:
                if command == 'R':
                    l, h = h, l
                elif command == 'D':
                    if l < h:
                        l += 1
                    elif l > h:
                        l -= 1
                    else:
                        if isEmpty:
                            isError = True
                            break
                        else:
                            isEmpty = True

            if isError:
                ans = "error"
            elif isEmpty:
                ans = '[]'
            elif l < h:
                ans = AC[l:h + 1]
            elif l > h:
                if h == 0:
                    ans = AC[l::-1]
                else:
                    ans = AC[l:h-1:-1]
            else:
                ans = AC[l]

            res = "["
            for i in range(len(ans)):
                res += f"{ans[i]}"
                if i < len(ans)-1:
                    res += ','
                else:
                    res += ']'

        else:
            if 'D' not in p:
                res = "[]"

        print(res)


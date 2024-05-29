import sys

input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, input().strip().split()))

    ans = 0

    if N == 3:
        ans = max(arr)*2
    else:
        # 벌벌통
        for i in range(1, N):
            ans = max(ans, sum(arr) - arr[0] - arr[i] + sum(arr[i+1:]))

        # 벌통벌
        for i in range(1, N-1):
            ans = max(ans, sum(arr) - arr[0] - arr[-1] + arr[i])

        # 통벌벌
        for i in range(N-1):
            ans = max(ans, sum(arr) - arr[-1] - arr[i] + sum(arr[:i]))

    print(ans)

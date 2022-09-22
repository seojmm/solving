import sys
input = sys.stdin.readline

N = int(input())
H = list(map(int, input().split()))
arr = [0]*(N+1)

for cur in H:
    if arr[cur]:
        arr[cur] -= 1
        arr[cur-1] += 1
    else:
        arr[cur-1] += 1

print(sum(arr))
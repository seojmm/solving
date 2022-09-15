import sys
import collections
input = sys.stdin.readline

N, K = map(int, input().split())
belt = list(map(int, input().split()))
isOn = [False]*N
step = 0


def rotate():
    global belt, isOn
    tmp = []
    tmp.append(belt.pop())
    belt = tmp + belt

    tmp = []
    tmp.append(isOn.pop())
    isOn = tmp + isOn


while True:
    step += 1
    # step 1
    rotate()
    isOn[-1] = False

    # step 2
    for i in range(N-2, -1, -1):
        if isOn[i]:
            if not isOn[i+1] and belt[i+1]:
                isOn[i] = False
                isOn[i+1] = True
                belt[i+1] -= 1
        isOn[-1] = False

    # step 3
    if belt[0]:
        isOn[0] = True
        belt[0] -= 1

    # step 4
    if belt.count(0) >= K:
        break
print(step)

import sys
import itertools

input = sys.stdin.readline

digit2button = {
    0: [[1, 1, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1]],
    1: [[0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1]],
    2: [[1, 1, 1], [0, 0, 1], [1, 1, 1], [1, 0, 0], [1, 1, 1]],
    3: [[1, 1, 1], [0, 0, 1], [1, 1, 1], [0, 0, 1], [1, 1, 1]],
    4: [[1, 0, 1], [1, 0, 1], [1, 1, 1], [0, 0, 1], [0, 0, 1]],
    5: [[1, 1, 1], [1, 0, 0], [1, 1, 1], [0, 0, 1], [1, 1, 1]],
    6: [[1, 1, 1], [1, 0, 0], [1, 1, 1], [1, 0, 1], [1, 1, 1]],
    7: [[1, 1, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1]],
    8: [[1, 1, 1], [1, 0, 1], [1, 1, 1], [1, 0, 1], [1, 1, 1]],
    9: [[1, 1, 1], [1, 0, 1], [1, 1, 1], [0, 0, 1], [1, 1, 1]],
}

if __name__ == '__main__':
    N = int(input())
    state = []
    for i in range(5):
        line = input().strip()
        line = line.replace('#', '1')
        line = line.replace('.', '0')
        state.append(list(line))
    # print(state)
    cand_digits = []

    for i in range(0, 4*N - 1, 4):
        cand_digits.append([])
        cur_num = [row[i:i+3] for row in state]
        isCand = False

        for j in range(10):
            for r in range(5):
                for c in range(3):
                    if digit2button[j][r][c] == 0 and cur_num[r][c] == '1':
                        isCand = False
                        break
                    else:
                        isCand = True
                if not isCand:
                    break

            if isCand:
                cand_digits[-1].append(j)

    sum = 0
    if len(cand_digits[0]) == 0:
        sum = -1
    else:
        arr = [0 for _ in range(N)]

        for i in range(N):
            for j in range(len(cand_digits[i])):
                arr[i] += cand_digits[i][j]

        for i in range(N):
            if len(cand_digits[i]) == 0:
                sum = -1
                break

            sum *= 10
            sum += arr[i] / len(cand_digits[i])

    print(sum)


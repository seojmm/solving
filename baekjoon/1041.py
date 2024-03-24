import sys
import collections

input = sys.stdin.readline

ans = 0
min3_list = []

if __name__ == '__main__':
    N = int(input())
    dice = list(map(int, input().split()))

    if N == 1:
        dice.sort()
        for i in range(5):
            ans += dice[i]
    else:
        for i in range(3):
            min3_list.append(min(dice[i], dice[5-i]))
        min3_list.sort()

        dice_1 = min3_list[0]
        dice_2 = min3_list[0] + min3_list[1]
        dice_3 = sum(min3_list)

        cnt_1 = 4*(N-2)*(N-1) + (N-2)**2
        cnt_2 = 4*(N-1) + (N-2)*4
        cnt_3 = 4

        ans += dice_1*cnt_1 + dice_2*cnt_2 + dice_3*cnt_3

    print(ans)




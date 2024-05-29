import sys

input = sys.stdin.readline

if __name__ == '__main__':
    N, K = map(int, input().split())

    coord_rect = []
    area_list = [0]
    for i in range(N):
        tmp = list(map(int, input().split()))
        area = abs(tmp[1]-tmp[3])*abs(tmp[0]-tmp[2])
        area_list.append(area)

        for j in range(i-1, -1, -1):
            # 겹치는거 확인
            if coord_rect[j][0] <= tmp[0] <= coord_rect[j][2]:
                if coord_rect[j][1] <= tmp

        coord_rect.append(tmp)

    # i = 1
    # for coord in coord_rect:
    #
    #
    #     i += 1
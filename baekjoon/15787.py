import sys

input = sys.stdin.readline

N, M = map(int, input().split())

status = [[0]*20 for _ in range(N)]


for _ in range(M):
    cur_cmd = list(map(int, input().split()))

    if cur_cmd[0] == 1:
        status[cur_cmd[1]-1][cur_cmd[2]-1] = 1
    elif cur_cmd[0] == 2:
        status[cur_cmd[1]-1][cur_cmd[2]-1] = 0
    elif cur_cmd[0] == 3:
        status[cur_cmd[1]-1].pop()
        status[cur_cmd[1]-1].insert(0, 0)
    else:
        status[cur_cmd[1]-1].pop(0)
        status[cur_cmd[1]-1].append(0)


# result = []
# for i in range(N):
#     if status[i] not in result:
#         result.append(status[i])

# print(len(result))

result = set()
for i in range(N):
    result.add(tuple(status[i]))

print(len(result))
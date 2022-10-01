import copy

MAX_DIFF = 0
answers = []

# 점수차이 계산
def getScoreDiff(info, shots):
    ap, ry = 0, 0
    for i in range(11):
        if info[i] == shots[i] == 0:
            continue
        elif info[i] >= shots[i]:
            ap += 10-i
        else:
            ry += 10-i
    
    return ry-ap


def dfs(info, shots, n, i):
    global answers, MAX_DIFF

    if i == 11:
        if n != 0:
            shots[10] = n
        scoreDiff = getScoreDiff(info, shots)
        if scoreDiff <= 0: # 라이언 패
            return
        result = copy.deepcopy(shots)
        if scoreDiff > MAX_DIFF:
            answers = [result]
            MAX_DIFF = scoreDiff
            return
        elif scoreDiff == MAX_DIFF:
            answers.append(result)
        return
    
    # i점을 얻는 경우
    if info[i] < n:
        shots.append(info[i] + 1)
        dfs(info, shots, n-info[i]-1, i+1) # info[i]+1만큼 거기다 쏴야하니까.
        shots.pop()
    
    # i점을 포기하는 경우
    shots.append(0)
    dfs(info, shots, n, i+1)
    shots.pop()
            

def solution(n, info):
    global answers

    dfs(info, [], n, 0)
    if answers == []:
        return [-1]

    answers.sort(key=lambda x: x[::-1])

    return answers[-1]

print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
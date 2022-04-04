import sys
import collections

input = sys.stdin.readline

def solution(id_list, report, k):
    answer = [0]*len(id_list)
    dicSet = collections.defaultdict(list)

    for rep in report:
        tmpArr = rep.split()
        if not tmpArr[0] in dicSet[tmpArr[1]]:
            dicSet[tmpArr[1]].append(tmpArr[0])
    
    for k, v in dicSet.items():
        if len(v) >= 2:
            for name in v:
                answer[id_list.index(name)] += 1


    return answer

print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
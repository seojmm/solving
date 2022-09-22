import itertools
import collections

def solution(relation):
    answer = []
    row = len(relation)
    col = len(relation[0])
    
    #set_transformed = list(map(set, list(zip(*relation))))
    transformed = list(zip(*relation))
    c = []
    for i in range(1, col+1):
        c.extend(itertools.combinations(range(col), i))
    
    for com in c:
        tmp = []
        for key in com:
            tmp.append(transformed[key])
        tmp = list(zip(*tmp))
        #print(tmp)
        
        if len(set(tmp)) == row:
            canAdd = True
            for ans in answer:
                if set(ans).issubset(set(com)):
                    canAdd = False
                    break
            
            if canAdd:
                answer.append(com)
                #print(com)

    return len(answer)

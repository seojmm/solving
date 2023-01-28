import sys
import itertools

def solution(users, emoticons):
    answer = []
    discount = [40, 30, 20, 10]
    for p in itertools.product(discount, repeat=len(emoticons)):
        tmp = [0, 0]
        for ratio, capacity in users:
            sold = 0
            for emo, dc in zip(emoticons, p):
                if ratio <= dc:
                    sold += emo * (1 - dc/100)
            if sold >= capacity:
                tmp[0] += 1
            else:
                tmp[1] += sold
        answer = max(answer, tmp)
        
    
    return answer

print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
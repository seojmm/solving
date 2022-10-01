import collections

def solution(queue1, queue2):
    answer = 0
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    totalSum = sum1 + sum2
    if totalSum%2 == 1:
        return -1

    idx1, idx2 = 0, 0

    while True:
        if sum1 == sum2:
            break
        elif sum1 < sum2:
            if idx2 < len(queue2):
                sum1 += queue2[idx2]
                sum2 -= queue2[idx2]
            elif idx2 < len(queue2) + len(queue1):
                sum1 += queue1[idx2-len(queue2)]
                sum2 -= queue1[idx2-len(queue2)]
            else:
                return -1
            idx2 += 1
        else:
            if idx1 < len(queue1):
                sum2 += queue1[idx1]
                sum1 -= queue1[idx1]
            elif idx1 < len(queue1) + len(queue2):
                sum2 += queue2[idx1-len(queue1)]
                sum1 -= queue2[idx1-len(queue1)]
            else:
                return -1
            idx1 += 1

        answer += 1

    return answer

print(solution([1, 1], [1, 5]))


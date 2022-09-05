def solution(stones, k):
    lo = 0
    hi = max(stones)

    while lo <= hi:
        mid = lo + (hi - lo)//2
        arr = list(map(lambda x: x - mid, stones))
        cnt = 0
        for e in arr:
            if cnt < k:
                if e <= 0:
                    cnt += 1
                else:
                    cnt = 0
            else:
                break
        
        if cnt < k:
            lo = mid + 1
        else:
            hi = mid - 1
            answer = mid

    
    return answer
    

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
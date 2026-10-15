N, M = 4, 6
arr = [19, 15, 10, 17]

left, right = 0, max(arr)
answer = 0

while left <= right:
    mid = (left+right)//2
    total = 0

    for x in arr:
        if x > mid:
            total += x - mid
    
    if total < M:
        right = mid - 1
    else:
        answer = mid
        left = mid + 1

print(answer)
    
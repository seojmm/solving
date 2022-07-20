def solution(sizes):
    answer = 0
    for size in sizes:
        size.sort()
    sizes.sort(key=lambda x: (x[0], x[1]))
    ansSize = sizes[0]
    for size in sizes[1:]:
        if ansSize[0] < size[0]:
            ansSize[0] = size[0]
        if ansSize[1] < size[1]:
            ansSize[1] = size[1]

    answer = ansSize[0] * ansSize[1]
    return answer

print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))
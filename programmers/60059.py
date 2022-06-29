def fit(x, y, M, key, graph):
    for i in range(M):
        for j in range(M):
            graph[x+i][y+j] += key[i][j]

def unfit(x, y, M, key, graph):
    for i in range(M):
        for j in range(M):
            graph[x+i][y+j] -= key[i][j]

def rotate(arr):
    return list(zip(*arr[::-1]))

def check(graph, M, N):
    for i in range(N):
        for j in range(N):
            if graph[M+i][M+j] != 1:
                return False;
    return True

def solution(key, lock):
    M, N = len(key), len(lock)

    graph = [[0] * (M*2 + N) for _ in range(M*2 + N)]

    for i in range(N):
        for j in range(N):
            graph[M+i][M+j] = lock[i][j]

    rotated_key = key

    for _ in range(4):
        rotated_key = rotate(rotated_key)
        for x in range(1, M+N):
            for y in range(1, M+N):
   
                fit(x, y, M, rotated_key, graph)

                if(check(graph, M, N)):
                    return True

                unfit(x, y, M, rotated_key, graph)
                
    return False
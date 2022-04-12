import sys
import collections
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

K = int(input())
while(K):
    graph = collections.defaultdict(list)
    V, E = map(int, input().split())
    visited = [0]*(V+1)
    group = 1
    flag = True
    q = collections.deque()
    for i in range(E):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    
    for i in range(1, V+1):
        if visited[i] == 0:
            q.append(i)
            visited[i] = group
            while q and flag:
                x = q.popleft()
                for next in graph[x]:
                    if visited[next] == 0:
                        visited[next] = -visited[x]
                        q.append(next)
                    elif visited[x] == visited[next]:
                        flag = False
                        break
            
        if not flag:
            break

    if flag:
        print("YES")
    else:
        print("NO")

    


    K -= 1
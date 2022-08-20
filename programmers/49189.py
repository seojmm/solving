import collections

def solution(n, edge):
    answer = 0
    graph = collections.defaultdict(list)
    for u, v in edge:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False]*(n+1)
    maxDist = 0

    q = collections.deque()
    q.append((1, 0))
    visited[1] = True

    while q:
        node, weight = q.popleft()
        if weight > maxDist:
            maxDist = weight
            answer = 1
        elif weight == maxDist:
            answer += 1

        for next in graph[node]:
            if not visited[next]:
                q.append((next, weight+1))
                visited[next] = True

    return answer
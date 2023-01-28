import sys
import heapq
sys.setrecursionlimit(10**6)
answer = "~"
nd = ["d", "l", "r", "u"]
dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]
vec = []

def backtracking(n, m, curX, curY, r, c, route, k):
    global answer
    remain = abs(r-curX) + abs(c-curY)
    if len(route) + remain > k: return
    if len(route) == k and (curX, curY) == (r, c):
        #heapq.heappush(vec, route)
        answer = route
        return
    
    if 1 <= curX+1 <= n and 1 <= curY <= m and route < answer:
        backtracking(n, m, curX+1, curY, r, c, route+"d", k)
    if 1 <= curX <= n and 1 <= curY-1 <= m and route < answer:
        backtracking(n, m, curX, curY-1, r, c, route+"l", k)
    if 1 <= curX <= n and 1 <= curY+1 <= m and route < answer:
        backtracking(n, m, curX, curY+1, r, c, route+"r", k)
    if 1 <= curX-1 <= n and 1 <= curY <= m and route < answer:
        backtracking(n, m, curX-1, curY, r, c, route+"u", k)
            
def solution(n, m, x, y, r, c, k):
    
    remain = abs(r-x) + abs(c-y)
    # 이거 없으니까 마지막 테스트케이스가 시간초과
    if k < remain or (k-remain)%2 == 1:
        return "impossible"
    
    backtracking(n, m, x, y, r, c, "", k)
    
    #return heapq.heappop(vec)
    return answer
    
print(solution(2, 2, 2, 2, 1, 1, 4))
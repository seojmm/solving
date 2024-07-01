import sys

input = sys.stdin.readline

k = int(input())
A = list(input().strip().split())
min_ans, max_ans = "", ""
visited = [0 for _ in range(10)]

num_list = [str(i) for i in range(10)]

def check(prev, cur, ch):
    if ch == '<':
        return prev < cur
    else:
        return prev > cur

def backtracking(depth, s):
    global max_ans, min_ans
    if depth == k+1:
        if len(min_ans) == 0:
            min_ans = s
        else:
            max_ans = s

        return 

    for i in range(10):
        if not visited[i]:
            if depth == 0 or check(s[-1], str(i), A[depth-1]):
                visited[i] = True
                backtracking(depth+1, s+str(i))
                visited[i] = False

backtracking(0, "")
print(max_ans)
print(min_ans)
        
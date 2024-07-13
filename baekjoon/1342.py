import sys
input = sys.stdin.readline

ans = 0

def check(s):
    if len(s) == 1:
        return True
    
    for i in range(1, len(s)-1):
        if s[i] == s[i+1]:
            return False

    return True

def backtracking(depth, s, data, n):
    global ans
    
    if depth == n:
        ans += 1
        # print(s)
        return
        
    for key in data.keys():
        if len(s) == 0:
            data[key] -= 1
            backtracking(depth+1, s+key, data, n)
            data[key] += 1
            continue
        elif data[key] > 0 and key != s[-1]:
            data[key] -= 1
            backtracking(depth+1, s+key, data, n)
            data[key] += 1
            

raw = input().strip()
data = {}

for ch in raw:
    if ch not in data:
        data[ch] = 1
    else:
        data[ch] += 1

backtracking(0, "", data, len(raw))
print(ans)
import sys
input = sys.stdin.readline


def dfs(num, idx):
    global answer

    if num == K-5:
        cnt = 0
        for word in words:
            checked = True
            for w in word:
                if not learned[ord(w)-ord('a')]:
                    checked = False
                    break
            if checked: cnt += 1
        answer = max(answer, cnt)
        return
    
    for i in range(idx, 26):
        if not learned[i]:
            learned[i] = 1
            dfs(num+1, i)
            learned[i] = 0
    

answer = 0
N, K = map(int, input().split())
words = list(input().strip() for _ in range(N))
for i in range(N):
    words[i] = words[i][4:-4]

learned = [0]*26
for ch in ['a', 'c', 'i', 'n', 't']:
    learned[ord(ch) - ord('a')] = 1

if K <= 4:
    print(0)
else:
    dfs(0, 0)
    print(answer)
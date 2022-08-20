import sys
import collections
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

while True:
    try:
        block = []
        x = int(input())*10000000
        n = int(input())
        
        for _ in range(n):
            tmp = int(input())
            block.append(tmp)
        block.sort()

        l, r = 0, n-1
        ans = [-1000000001, -1000000001]

        while True:
            while l < r:
                if block[l] + block[r] == x:
                    ans = block[l], block[r]
                    break
                elif block[l] + block[r] < x:
                    l += 1
                else:
                    r -= 1

            if ans == [-1000000001, -1000000001]:
                print("danger")
                break
            else:
                print("yes", ans[0], ans[1])
                break
    except:
        break
    


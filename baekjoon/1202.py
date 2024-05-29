import sys
import heapq
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

N, K = 0, 0
ans = 0

if __name__ == '__main__':
    N, K = map(int, input().split())
    jewelry = [list(map(int, input().split())) for _ in range(N)]
    capacity = [int(input().strip()) for _ in range(K)]

    jewelry.sort()
    capacity.sort()

    heap = []
    for cap in capacity:
        while jewelry and jewelry[0][0] <= cap:
            heapq.heappush(heap, -jewelry[0][1])
            heapq.heappop(jewelry)
        if heap:
            ans -= heapq.heappop(heap)

    print(ans)




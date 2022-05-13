import sys
import heapq
import collections
input = sys.stdin.readline

pq = collections.deque()
T = int(input())
while(T):
    T -= 1
    pq.clear()
    h, w = map(int, input().split())
    prison = []
    for i in range(h):
        prison.append(list(input().rstrip()))
    
    
    
    
    

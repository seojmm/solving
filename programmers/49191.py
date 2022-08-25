import sys
import collections


def solution(n, results):
    answer = 0
    win = collections.defaultdict(set)
    lose = collections.defaultdict(set)

    for result in results:
        win[result[1]].add(result[0])
        lose[result[0]].add(result[1])

    for i in range(1, n+1):
        for winner in win[i]:
            lose[winner].update(lose[i])
        for loser in lose[i]:
            win[loser].update(win[i])

    for i in range(1, n+1):
        if len(win[i]) + len(lose[i]) == n-1:
            answer += 1

    return answer

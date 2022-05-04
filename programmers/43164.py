<<<<<<< HEAD
import collections
import sys


def solution(tickets):
    answer = []

    graph = collections.defaultdict(list)
    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])
    for val in graph:
        
    # def dfs(departure, arrival, tmp):

    return answer


solution([["ICN", "SFO"], ["ICN", "ATL"], [
         "SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]])
=======
import sys
import collections

def solution(tickets):
    answer = []
    graph = collections.defaultdict(list)

    for ticket in sorted(tickets):
        graph[ticket[0]].append(ticket[1])
    
    def dfs(v):
        while graph[v]:
            dfs(graph[v].pop(0))
        answer.append(v)
    
    dfs("ICN")

    return answer[::-1]
>>>>>>> 59622aad575bf258121efa9a4ebb2e954fa1f84c

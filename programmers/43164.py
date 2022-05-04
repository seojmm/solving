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

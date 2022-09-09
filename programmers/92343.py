import collections
                
def solution(info, edges):
    answer = []
    visited = [False]*len(info)
    visited[0] = True

    def dfs(sheep, wolf):
        if sheep > wolf:
            answer.append(sheep)
        else:
            return

        for i in range(len(edges)):
            parent = edges[i][0]
            child = edges[i][1]
            if visited[parent] and not visited[child]:
                visited[child] = True
                if info[child] == 0:
                    dfs(sheep+1, wolf)
                else:
                    dfs(sheep, wolf+1)
                visited[child] = False
            

    dfs(1, 0)
    
    return max(answer)
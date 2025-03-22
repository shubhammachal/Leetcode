class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #create adjacency list
        graph = [[] for _ in range(n)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        count = 0

        def dfs(vertex):
            #mark visited of vertex = True
            visited[vertex] = True
            #graph[vertex] retrieves the list of all neighbors (adjacent vertices) 
            #for the current vertex from our adjacency list.
            for neighbor in graph[vertex]:
                if not visited[neighbor]:
                    dfs(neighbor)

        for vertex in range(n):
            if not visited[vertex]:
            #number of components are number of times we have to perform DFS
                count += 1
                dfs(vertex)


        return count
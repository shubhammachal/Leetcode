class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #inuition : if cycle, can't finish
        #Approach - build graph
        # recursive dfs for cycle detection
        graph = {i:[] for i in range(numCourses)}

        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        # dfs
        states = {vertex:0 for vertex in graph}
        def dfs(vertex):
            states[vertex] = 1
            for neighbor in graph[vertex]:
                if states[neighbor] == 0:
                    if dfs(neighbor):
                        return True
                elif states[neighbor] == 1:
                    return True
            states[vertex] = 2
            return False

        for vertex in graph:
            if states[vertex] == 0:
                if dfs(vertex):
                    return False
        return True


        



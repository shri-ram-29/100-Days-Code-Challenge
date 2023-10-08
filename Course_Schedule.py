class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        visited = [0] * numCourses
        
        def isCyclic(course):
            if visited[course] == -1:
                return True
            if visited[course] == 1:
                return False
            
            visited[course] = -1
        
            for prereq in graph[course]:
                if isCyclic(prereq):
                    return True

            visited[course] = 1
            return False
        for i in range(numCourses):
            if isCyclic(i):
                return False
        
        return True

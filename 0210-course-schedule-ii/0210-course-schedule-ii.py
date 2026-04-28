class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[]*numCourses for _ in range(numCourses)]
        indgree = [0]*numCourses
        for a,b in prerequisites:
            graph[b].append(a)
            indgree[a] += 1

        q =deque()
        for i in range(numCourses):
            if indgree[i] == 0:
                q.append(i)
        ans = []
       

        # visitd = [0]*numCourses
        # visited[0] = 1
        while q:
            node = q.popleft()
            ans.append(node)
            for i in graph[node]:
                indgree[i] -= 1
            
            for neigh in graph[node]:
                if indgree[neigh] == 0:
                    q.append(neigh)
        if len(ans) == numCourses:
            return ans

        return [] 


                  

    


        
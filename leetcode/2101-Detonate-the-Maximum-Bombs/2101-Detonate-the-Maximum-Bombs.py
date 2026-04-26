class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i in range(len(bombs)):
            for j in range(i+1,len(bombs)):
                x1,y1,r1 = bombs[i]
                x2,y2,r2 = bombs[j]
                d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
                if r1 >= d:
                    graph[i].append(j)

                if r2 >= d:
                    graph[j].append(i)

        
        stack = []
        max_val =[1]

        def dfs(i):
            visited = set([i])
            temp = 1
            while stack:
               i = stack.pop()
               for neigh in graph[i]:
                    if neigh not in visited:
                        temp += 1
                        visited.add(neigh)
                        stack.append(neigh)

            max_val[0] = max(max_val[0],temp)
       
        for i in range(len(bombs)):
                stack.append(i)
                dfs(i)

        return max_val[0]
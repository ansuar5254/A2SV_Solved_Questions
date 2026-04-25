class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graphr = defaultdict(list)
        graphb = defaultdict(list)
        for s,d in redEdges:
            graphr[s].append(d)

        for s,d in blueEdges:
            graphb[s].append(d)


        visited = set()

        red = 1
        blue = 2

        q = deque()
        q.append((0,0,0))
        visited.add((0,0))
        ans = [-1]*n

        while q:
                node,length,color= q.popleft()
                if ans[node] == -1:
                    ans[node] = length
                if color != red:
                    for neigh in graphr[node]:
                        if (neigh,red) not in visited:
                            visited.add((neigh,red))
                            q.append((neigh,length+1,red))

                if color != blue:
                    for neigh in graphb[node]:
                        if (neigh,blue) not in visited:
                            visited.add((neigh,blue))
                            q.append((neigh,length+1,blue))

        return ans

                        

        
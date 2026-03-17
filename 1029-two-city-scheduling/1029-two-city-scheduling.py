class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        index = []
        diff = []
        for i in range(len(costs)):
            diff.append([costs[i][1]-costs[i][0],i])

        diff.sort()
        for val,ind in diff:
            index.append(ind)

        l = 0
        r = len(costs)-1
        total = 0
        while l < r:
            total += costs[index[l]][1]
            total += costs[index[r]][0]
            l += 1
            r -= 1
        return total
      
            



            
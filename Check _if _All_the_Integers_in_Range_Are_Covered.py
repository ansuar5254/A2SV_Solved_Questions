class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for i in range(left,right + 1):
            flag = False
            for j in range(len(ranges)):
                if ranges[j][0] <= i <= ranges[j][1]:
                    flag = True
            if flag == False:
                return False
        return True
                
        

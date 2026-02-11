

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count = Counter(s)
        t_count = Counter(t)
        min_num = 0
        for key,value in s_count.items():
            if key in t_count:
                if s_count[key] > t_count[key]:
                    min_num += (s_count[key]-t_count[key])
            else:
                min_num += s_count[key] 
        return min_num
            




        

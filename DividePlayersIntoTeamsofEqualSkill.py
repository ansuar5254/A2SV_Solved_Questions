class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l = 0
        r = len(skill)-1
        pre = skill[l] + skill[r]
        pro = skill[l] * skill[r]
        l += 1
        r -= 1
        
        while l < r:
            if pre == skill[l]+skill[r]:
                pro += (skill[l]*skill[r])
                l += 1
                r -= 1
            else:
                return -1
        return pro

            
            

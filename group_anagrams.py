class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sdict = {}
        for s in strs:
            ss = ''.join(sorted(s))
            if ss not in sdict:
                sdict[ss] = []
            sdict[ss].append(s)
        result = []
        for i in sdict:
            result.append(sdict[i])
        return result
            

        
        

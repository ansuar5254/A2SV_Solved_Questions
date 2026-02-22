class Solution:
    def customSortString(self, order: str, s: str) -> str:
        index = {}
        count = Counter(s)
        result  = []
        for i in order:
            if i in count:
                result.append(i*count[i])
                del count[i]
        remain = []
        for key,value in count.items():
            remain.append(key*value)
        return ''.join(result) + ''.join(remain)
            

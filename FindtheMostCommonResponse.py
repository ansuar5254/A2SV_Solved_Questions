class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        count = {}
        for i in range(len(responses)):
            checker = set()
            for j in range(len(responses[i])):
                    if responses[i][j] not in checker:
                        checker.add(responses[i][j])
                        count[responses[i][j]] = count.get(responses[i][j],0)+1
        sorted_response = sorted(count.items(),key = lambda x :(-x[1],x[0]))
        for key,value in sorted_response:
            return key
            break

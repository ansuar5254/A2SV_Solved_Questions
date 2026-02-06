class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict1 = {}
        dict2 = {}
        rDict = {}
        for index,value in enumerate(list1):
            dict1[value] = index
        for index,value in enumerate(list2):
            dict2[value] = index
        for s in list1:
            if s in dict2:
                rDict[s] = dict1[s]+dict2[s]
        sorted_value  = sorted(rDict.items(),key = lambda x:x[1])
        result = []
        c = sorted_value[0][1]
        for s,ind in sorted_value:
            if ind == c:
                result.append(s)
        return result
        
        

        
    
                





        
        

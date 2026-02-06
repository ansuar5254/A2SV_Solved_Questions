class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        path_dict = {}
        n = len(paths)
        for i in range(n):
            l = 0
            key = []
            flag1 = True
            firstdir = ''
            for j in range(len(paths[i])):
                if flag1 and paths[i][j] == ' ':
                    firstdir = paths[i][l:j]
                    l = j+1
                    flag1 = False
                if paths[i][j] == '(':
                        key.append(firstdir + '/'+ paths[i][l:j])
                        l = j+1
                if paths[i][j] == ')':
                    key.append(paths[i][l:j])
                    l = j+2
            r = 0
            while r < len(key)-1:
                if key[r+1] in path_dict:
                      path_dict[key[r+1]].append(key[r])
                else:
                     path_dict[key[r+1]] = []
                     path_dict[key[r+1]].append(key[r])
                r += 2
        result = []
        for value in path_dict.values():
            if len(value)>1:
                result.append(value)
        return result




        
        
            
            


            

                





        
        
        

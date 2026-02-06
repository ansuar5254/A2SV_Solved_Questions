class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_dict = Counter(chars)
        result = 0
        for s in words:
            flag = True
            dicts = Counter(s)
            for ch,fre  in dicts.items():
                if ch not in char_dict:
                    flag = False
                    break
                else:
                    if fre > char_dict[ch]:
                        flag = False
                        break
            if flag:
                result += len(s)
        return result


            


        
        

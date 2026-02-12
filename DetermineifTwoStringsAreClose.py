class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        count1 = Counter(word1)
        count2 = Counter(word2)
        fre1 = []
        fre2 = []
        w1 = []
        w2 = []
        for key,val in count1.items():
            fre1.append(val)
            w1.append(key)
        for key,val in count2.items():
            fre2.append(val)
            w2.append(key)
        fre1.sort()
        fre2.sort()
        w1.sort()
        w2.sort()
        return fre1 == fre2 and w1==w2

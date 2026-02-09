import random

class RandomizedSet:

    def __init__(self):
        self.a = []    
        self.m = {}     
    def insert(self, v: int) -> bool:
        if v in self.m:
            return False
        self.m[v] = len(self.a)
        self.a.append(v)
        return True
    def remove(self, v: int) -> bool:
        if v not in self.m:
            return False
        i = self.m[v]
        x = self.a[-1]
        self.a[i] = x
        self.m[x] = i
        self.a.pop()
        del self.m[v]
        return True
    def getRandom(self) -> int:
        return random.choice(self.a)

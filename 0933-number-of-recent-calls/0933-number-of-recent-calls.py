class RecentCounter:

    def __init__(self):
        self.arr = []
    def ping(self, t: int) -> int:
        self.arr.append(t)
        l = 0
        while self.arr and t - 3000 > self.arr[l]:
            l += 1
        return len(self.arr) - l
        
        


        
        
        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
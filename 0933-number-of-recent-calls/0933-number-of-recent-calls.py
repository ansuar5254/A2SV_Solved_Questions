class RecentCounter:

    def __init__(self):
        self.arr = []
        self.l = 0
    def ping(self, t: int) -> int:
        self.arr.append(t)
        while self.arr and t - 3000 > self.arr[self.l]:
            self.l += 1
        return len(self.arr) - self.l

        


        
        
        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
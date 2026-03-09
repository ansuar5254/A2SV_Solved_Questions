class RecentCounter:

    def __init__(self):
        self.q = deque()
    def ping(self, t: int) -> int:
        self.q.append(t)
        if t-3000 <= self.q[0]:
            return len(self.q)
           
        else:
            while t-3000 > self.q[0]:
                    self.q.popleft()
            return len(self.q)
        
        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
class DataStream:

    def __init__(self, value: int, k: int):
        self.q = deque()
        self.k = k
        self.val = value
    def consec(self, num: int) -> bool:
        if num == self.val:
            self.q.append(num)
        else:
            while self.q:
                self.q.popleft()

        if len(self.q) >= self.k:
            return True
        else:
            return False


        
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
class RecentCounter:

    def __init__(self):
        import collections
        self.C = collections.deque()

    def ping(self, t: int) -> int:
        self.C.append(t)
        while self.C[0] < t - 3000:
            self.C.popleft()
        return len(self.C)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

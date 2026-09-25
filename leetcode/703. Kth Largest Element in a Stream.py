import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.h = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        (heapq.heappush if len(self.h) < self.k else heapq.heappushpop)(self.h, val)
        return self.h[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

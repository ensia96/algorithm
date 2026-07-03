class NumArray:

    def __init__(self, nums: List[int]):
        self.A = [0]
        for n in nums:
            self.A += self.A[-1] + n,

    def sumRange(self, left: int, right: int) -> int:
        return self.A[right + 1] - self.A[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

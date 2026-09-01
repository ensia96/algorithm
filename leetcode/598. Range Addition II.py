class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        return ops and min(o[0] for o in ops) * min(o[1] for o in ops) or m * n

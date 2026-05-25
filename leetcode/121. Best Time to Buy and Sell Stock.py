class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m, M = 10000, 0
        for p in prices:
            m = min(m, p)
            M = max(M, p - m)
        return M

class Solution:
    def climbStairs(self, n: int) -> int:
        a = b = 1
        for _ in ' ' * n:
            a, b = b, a + b
        return a

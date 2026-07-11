class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 0, num
        while l <= r:
            m = (l + r) // 2
            M = m * m
            if M == num:
                return True
            elif M < num:
                l = m + 1
            else:
                r = m - 1
        return False

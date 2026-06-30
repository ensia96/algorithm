# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        while l < r:
            l, r = [((m := l + (r - l) // 2) + 1, r), (l, m)][isBadVersion(m)]
        return l

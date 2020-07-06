class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        i = 0
        while m != n:
            m >>= 1
            n >>= 1
            i += 1
        return n << i


# Success
# Details
# Runtime: 96 ms, faster than 14.18% of Python3 online submissions for Bitwise AND of Numbers Range.
# Memory Usage: 13.7 MB, less than 90.52% of Python3 online submissions for Bitwise AND of Numbers Range.
# ================================================#
#     ^ my answer      ||  most voted answer v   #
# ================================================#


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if len(bin(m)) != len(bin(n)):
            return 0
        for i in range(m + 1, n + 1):
            m &= i
        return m


# ================================================#
#                  question v                     #
# ================================================#

# 201. Bitwise AND of Numbers Range
# Medium

# Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

# Example 1:

# Input: [5,7]
# Output: 4
# Example 2:

# Input: [0,1]
# Output: 0

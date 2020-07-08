class Solution:
    def isHappy(self, n: int) -> bool:
        i = 0
        while i < 10:
            n = sum(int(i) ** 2 for i in str(n))
            if n == 1:
                return True
            i += 1
        return False


# Success
# Details
# Runtime: 44 ms, faster than 26.81% of Python3 online submissions for Happy Number.
# Memory Usage: 13.9 MB, less than 44.48% of Python3 online submissions for Happy Number.
# ================================================#
#     ^ my answer      ||  most voted answer v   #
# ================================================#


class Solution:
    def isHappy(self, n):
        seen = set()
        while n not in seen:
            seen.add(n)
            n = sum([int(x) ** 2 for x in str(n)])
        return n == 1


# ================================================#
#                  question v                     #
# ================================================#

# 202. Happy Number
# Easy

# Write an algorithm to determine if a number n is "happy".

# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

# Return True if n is a happy number, and False if not.

# Example:

# Input: 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

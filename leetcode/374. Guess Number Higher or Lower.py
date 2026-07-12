# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is lower than the guess number
#          1 if num is higher than the guess number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            m = l + (r - l) // 2
            a = guess(m)
            if a == 0:
                return m
            elif a < 0:
                r = m - 1
            else:
                l = m + 1
        return -1

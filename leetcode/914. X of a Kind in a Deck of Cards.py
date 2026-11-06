class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        from collections import Counter
        from math import gcd
        return gcd(*Counter(deck).values()) >= 2

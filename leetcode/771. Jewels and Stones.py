class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        J = set(jewels)
        return sum(i in J for i in stones)

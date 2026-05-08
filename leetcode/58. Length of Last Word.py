class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        S = s.split()
        return len(S) and len(S[-1])

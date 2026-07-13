class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter as C
        return not (C(ransomNote) - C(magazine))

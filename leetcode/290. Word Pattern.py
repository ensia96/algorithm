class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        return len(pattern) == len(w := s.split()) and len(set(pattern)) == len(set(w)) == len(set(zip(pattern, w)))

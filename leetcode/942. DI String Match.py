class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        m, M = -1, len(s) + 1
        return [(m := m + 1) if char == 'I' else (M := M - 1)for char in s + 'I']

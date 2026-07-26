class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = 0
        for c in s:
            i += i < len(g) and c >= g[i]
        return i

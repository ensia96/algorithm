class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        l, c = 1, 0
        for i in s:
            w = widths[ord(i) - 97]
            if c + w > 100:
                l += 1
                c = 0
            c += w
        return [l, c]

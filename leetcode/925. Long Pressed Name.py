class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, n, p = 0, len(name), None
        for c in typed:
            if i < n and c == name[i]:
                i += 1
            elif c != p:
                return False
            p = c
        return i == n

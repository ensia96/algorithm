class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        while j < len(t) and i < len(s):
            i += s[i] == t[j]
            j += 1
        return i == len(s)

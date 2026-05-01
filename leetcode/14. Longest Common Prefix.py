class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        f = 1
        return ''.join(i[0] * (f := f * (len({*i}) < 2)) for i in zip(*strs))

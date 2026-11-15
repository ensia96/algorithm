class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        return sum(any(strs[i + 1][j] < strs[i][j] for i in range(len(strs) - 1)) for j in range(len(strs[0])))

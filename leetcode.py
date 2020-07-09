class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        from math import sqrt

        squares = [0]
        self.matrix, self.max_m, self.max_n = (
            matrix,
            len(matrix[0]),
            len(matrix),
        )
        max_m, max_n = self.max_m, self.max_n
        for m in range(max_m):
            for n in range(max_n):
                if int(matrix[n][m]):
                    size = self.isSquare(m, n)
                    print(m, n, size)
                    if sqrt(size) == int(sqrt(size)):
                        squares.append(size)
        return max(squares)

    def isSquare(self, m, n):
        matrix, max_m, max_n = self.matrix, self.max_m, self.max_n
        size = 1
        if m + 1 < max_m and n + 1 < max_n:
            if (
                int(matrix[n + 1][m])
                and int(matrix[n][m + 1])
                and int(matrix[n + 1][m + 1])
            ):
                size += self.isSquare(n + 1, m)
                size += self.isSquare(n, m + 1)
                size += self.isSquare(m + 1, n + 1)
        return size


#
#
#
#
# ================================================#
#     ^ my answer      ||  most voted answer v   #
# ================================================#


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        dp = [0] * (len(matrix[0]) + 1)
        maxLen = prev = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                temp = dp[j + 1]
                if matrix[i][j] == "1":
                    dp[j + 1] = min(prev, dp[j], dp[j + 1]) + 1
                    maxLen = max(maxLen, dp[j + 1])
                else:
                    dp[j + 1] = 0
                prev = temp
        return maxLen * maxLen


# ================================================#
#                  question v                     #
# ================================================#

# 221. Maximal Square
# Medium

# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

# Example:

# Input:

# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0

# Output: 4

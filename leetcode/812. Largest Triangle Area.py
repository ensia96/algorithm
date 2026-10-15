class Solution:
    def largestTriangleArea(self, points: list[list[int]]) -> float:
        A, n = 0, len(points)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    a, b, c, d, e, f = *points[i], *points[j], *points[k]
                    A = max(A, abs(a * (d - f) + c * (f - b) + e * (b - d)))
        return A / 2

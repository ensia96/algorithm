class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        return [[mat[(x := i * c + j) // n][x % n] for j in range(c)] for i in range(r)]if len(mat) * (n := len(mat[0])) == r * c else mat

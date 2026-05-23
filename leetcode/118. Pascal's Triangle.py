class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        A = [[1]]
        for _ in ' ' * ~-numRows:
            A += [[1] + [i + j for i, j in zip(A[-1], A[-1][1:])] + [1]]
        return A[:numRows]

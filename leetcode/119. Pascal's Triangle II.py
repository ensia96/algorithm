class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        A = [1]
        for _ in ' ' * rowIndex:
            A = [1] + [i + j for i, j in zip(A, A[1:])] + [1]
        return A

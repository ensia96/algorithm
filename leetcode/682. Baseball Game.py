class Solution:
    def calPoints(self, operations: List[str]) -> int:
        A = []
        for i in operations:
            if i == "C":
                A.pop()
            else:
                A.append(2 * A[-1] if i == "D" else A[-1] +
                         A[-2] if i == "+" else int(i))
        return sum(A)

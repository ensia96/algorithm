class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        A = []
        for i in range(left, right + 1):
            j = i
            while j and j % 10 and i % (j % 10) == 0:
                j //= 10
            if not j:
                A.append(i)
        return A

class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        A, i = [], len(num) - 1
        while i >= 0 or k:
            if i >= 0:
                k += num[i]
            k, j = divmod(k, 10)
            A.append(j)
            i -= 1
        A.reverse()
        return A

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        D = {}
        for i in licensePlate.lower():
            if i.isalpha():
                D[i] = D.get(i, 0) + 1
        A = ''
        for I in words:
            if A and len(I) >= len(A):
                continue
            d = {}
            for i in I:
                d[i] = d.get(i, 0) + 1
            if all(d.get(i, 0) >= c for i, c in D.items()):
                A = I
        return A

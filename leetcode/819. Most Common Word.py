class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        B = {*banned}
        C = {}
        for w in ''.join(i if i.isalpha()else ' 'for i in paragraph).lower().split():
            if w not in B:
                C[w] = C.get(w, 0) + 1
        return max(C, key=C.get)

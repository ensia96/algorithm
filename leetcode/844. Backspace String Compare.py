class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def f(I):
            S = []
            for i in I:
                if i == '#':
                    S and S.pop()
                else:
                    S.append(i)
            return ''.join(S)
        return f(s) == f(t)

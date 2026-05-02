class Solution:
    def isValid(self, s: str) -> bool:
        S = []
        D = {')': '(', '}': '{', ']': '['}
        for i in s:
            if i in D:
                x = S and S.pop()
                if x != D[i]:
                    return False
            else:
                S += i,
        return not S

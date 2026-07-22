class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n, m = len(num1), len(num2)
        i = c = 0
        A = []
        while (x := i < n) + (y := i < m) + c:
            c, d = divmod((x and int(num1[-i - 1])) +
                          (y and int(num2[-i - 1])) + c, 10)
            A.append(str(d))
            i += 1
        A.reverse()
        return ''.join(A)

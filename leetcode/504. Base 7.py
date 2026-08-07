class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        i = abs(num)
        a = []
        while i > 0:
            a.append(str(i % 7))
            i //= 7
        a.reverse()
        return "-" * (num < 0) + "".join(a)

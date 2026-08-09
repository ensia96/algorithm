class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        return num == sum((i + num // i * (i * i < num)) * (num % i < 1) for i in range(2, int(num ** .5) + 1)) + (num > 1)

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        c, l, p = 0, len(flowerbed), -2
        for i in range(l):
            if flowerbed[i] == 1:
                c, p = c + (i - p - 2) // 2, i
        return c + (l - p - 1) // 2 >= n

class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        return [[1 - i for i in l[::-1]]for l in image]

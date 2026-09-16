class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        return [[sum(v := [img[x][y] for x in range(max(0, i - 1), min(m, i + 2)) for y in range(max(0, j - 1), min(n, j + 2))]) // len(v) for j in range(n)] for i in range(m)]

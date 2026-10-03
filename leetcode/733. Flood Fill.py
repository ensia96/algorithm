class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        S, O, R, C = [(sr, sc)], image[sr][sc], len(image), len(image[0])
        if O == color:
            return image
        image[sr][sc] = color
        while S:
            r, c = S.pop()
            for i, j in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= i < R and 0 <= j < C and image[i][j] == O:
                    image[i][j] = color
                    S.append((i, j))
        return image

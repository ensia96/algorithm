class Solution:
    def numRookCaptures(self, board: list[list[str]]) -> int:
        B = ''.join(map(''.join, board))
        x, y = divmod(B.index('R'), 8)
        R = B[x * 8:x * 8 + 8]
        C = B[y::8]
        return sum((R[y + 1:].lstrip('.')[:1] == 'p', R[:y].rstrip('.')[-1:] == 'p', C[x + 1:].lstrip('.')[:1] == 'p', C[:x].rstrip('.')[-1:] == 'p'))

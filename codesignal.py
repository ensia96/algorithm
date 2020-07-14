def chessKnight(cell):
    from string import ascii_lowercase

    x = list(ascii_lowercase[:8])
    y = list(range(1, 9))
    cell_x = x.index(cell[0]) + 1
    cell_y = int(cell[1])

    def check_y1(x):
        answer = 0
        if x in y:
            if cell_y + 1 in y:
                answer += 1
            if cell_y - 1 in y:
                answer += 1
        return answer

    def check_y2(x):
        answer = 0
        if x in y:
            if cell_y + 2 in y:
                answer += 1
            if cell_y - 2 in y:
                answer += 1
        return answer

    return (
        check_y1(cell_x - 2)
        + check_y1(cell_x + 2)
        + check_y2(cell_x - 1)
        + check_y2(cell_x + 1)
    )


# ================================================#
#     ^ my answer      ||  most voted answer v   #
# ================================================#


def chessKnight(c):
    x, y = ord(c[0]) - 96, int(c[1])
    return (
        sum(
            [
                1 <= (x + i) <= 8 and 1 <= (y + j) <= 8
                for i in [-2, -1, 1, 2]
                for j in [-2, -1, 1, 2]
            ]
        )
        // 2
    )


# def chessKnight(cell):
#     r = 0
#     c = [ord(cell[0])-96,int(cell[1])]

#     m = [[1,2],[2,1],[1,-2],[-2,1],[-1,2],[2,-1],[-1,-2],[-2,-1]]

#     for i in m:
#         if 0<c[0]+i[0]<9 and 0<c[1]+i[1]<9:
#             r +=1
#     return r

# ================================================#
#                 question v                     #
# ================================================#

# Given a string, return its encoding defined as follows:

# First, the string is divided into the least possible number of disjoint substrings consisting of identical characters
# for example, "aabbbc" is divided into ["aa", "bbb", "c"]
# Next, each substring with length greater than one is replaced with a concatenation of its length and the repeating character
# for example, substring "bbb" is replaced by "3b"
# Finally, all the new strings are concatenated together in the same order and a new string is returned.
# Example

# For s = "aabbbc", the output should be
# lineEncoding(s) = "2a3bc".

# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] string s

# String consisting of lowercase English letters.

# Guaranteed constraints:
# 4 ≤ s.length ≤ 15.

# [output] string

# Encoded version of s.

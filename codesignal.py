def chessBoardCellColor(cell1, cell2):
    x = lambda x: True if x[0] in ["A", "C", "E", "G"] else False
    y = lambda x: True if int(x[1]) % 2 == 1 else False
    return (x(cell1) == y(cell1)) == (x(cell2) == y(cell2))


# ================================================#
#     ^ my answer      ||  most voted answer v   #
# ================================================#


def chessBoardCellColor(cell1, cell2):

    return (ord(cell1[0]) + int(cell1[1]) + ord(cell2[0]) + int(cell2[1])) % 2 == 0


# ================================================#
#                 question v                     #
# ================================================#

# Given two cells on the standard chess board, determine whether they have the same color or not.

# Example

# For cell1 = "A1" and cell2 = "C3", the output should be
# chessBoardCellColor(cell1, cell2) = true.


# For cell1 = "A1" and cell2 = "H3", the output should be
# chessBoardCellColor(cell1, cell2) = false.


# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] string cell1

# Guaranteed constraints:
# cell1.length = 2,
# 'A' ≤ cell1[0] ≤ 'H',
# 1 ≤ cell1[1] ≤ 8.

# [input] string cell2

# Guaranteed constraints:
# cell2.length = 2,
# 'A' ≤ cell2[0] ≤ 'H',
# 1 ≤ cell2[1] ≤ 8.

# [output] boolean

# true if both cells have the same color, false otherwise.

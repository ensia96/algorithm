def deleteDigit(n):
    return max(
        int("".join(v for j, v in enumerate(str(n)) if i != j))
        for i, _ in enumerate(str(n))
    )


# ================================================#
#     ^ my answer      ||  most voted answer v   #
# ================================================#


def deleteDigit(n):
    n = str(n)
    return max(int("".join(n[:i] + n[i + 1 :])) for i in range(len(n)))


# ================================================#
#                 question v                     #
# ================================================#

# Given some integer, find the maximal number you can obtain by deleting exactly one digit of the given number.

# Example

# For n = 152, the output should be
# deleteDigit(n) = 52;
# For n = 1001, the output should be
# deleteDigit(n) = 101.
# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] integer n

# Guaranteed constraints:
# 10 ≤ n ≤ 106.

# [output] integer

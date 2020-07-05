def digitDegree(n):
    i = 0
    if len(str(n)) == 1:
        return 0
    while True:
        a = 0
        for _ in str(n):
            a += int(_)
        n = a
        i += 1
        if len(str(a)) == 1:
            return i


# ================================================#
#     ^ my answer      ||  most voted answer v   #
# ================================================#


def digitDegree(n):
    if n < 10:
        return 0
    sumOfDigits = sum([int(i) for i in str(n)])
    return digitDegree(sumOfDigits) + 1


# def digitDegree(n):
#     d=0
#     while n>=10:
#         n=sum([int(i) for i in str(n)])
#         d+=1
#     return d

# ================================================#
#                 question v                     #
# ================================================#

# Let's define digit degree of some positive integer as the number of times we need to replace this number with the sum of its digits until we get to a one digit number.

# Given an integer, find its digit degree.

# Example

# For n = 5, the output should be
# digitDegree(n) = 0;
# For n = 100, the output should be
# digitDegree(n) = 1.
# 1 + 0 + 0 = 1.
# For n = 91, the output should be
# digitDegree(n) = 2.
# 9 + 1 = 10 -> 1 + 0 = 1.
# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] integer n

# Guaranteed constraints:
# 5 ≤ n ≤ 109.

# [output] integer

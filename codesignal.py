def arrayMaxConsecutiveSum(inputArray, k):
    max_v = sum(inputArray[0:k])
    l = len(inputArray)
    last_v = max_v
    for i in range(k, l):
        last_v = last_v + inputArray[i] - inputArray[i - k]
        if max_v < last_v:
            max_v = last_v
    return max_v

    # return max(sum(inputArray[i:i+k]) for i in range(len(inputArray)-k))
    # too slow...


# ================================================#
#     ^ my answer      ||  most voted answer v   #
# ================================================#


def arrayMaxConsecutiveSum(a, k):
    c = m = sum(a[:k])

    for i in range(len(a) - k):
        c = c + a[i + k] - a[i]
        m = max(c, m)

    return m

    # s = m = sum(inputArray[:k])
    # for i in range(k, len(inputArray)):
    #     s += inputArray[i] - inputArray[i-k]
    #     if s > m: m = s
    # return m


# ================================================#
#                 question v                     #
# ================================================#

# Given array of integers, find the maximal possible sum of some of its k consecutive elements.

# Example

# For inputArray = [2, 3, 5, 1, 6] and k = 2, the output should be
# arrayMaxConsecutiveSum(inputArray, k) = 8.
# All possible sums of 2 consecutive elements are:

# 2 + 3 = 5;
# 3 + 5 = 8;
# 5 + 1 = 6;
# 1 + 6 = 7.
# Thus, the answer is 8.
# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] array.integer inputArray

# Array of positive integers.

# Guaranteed constraints:
# 3 ≤ inputArray.length ≤ 105,
# 1 ≤ inputArray[i] ≤ 1000.

# [input] integer k

# An integer (not greater than the length of inputArray).

# Guaranteed constraints:
# 1 ≤ k ≤ inputArray.length.

# [output] integer

# The maximal possible sum.

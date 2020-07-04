def knapsackLight(value1, weight1, value2, weight2, maxW):
    bag = {"value": 0, "weight": 0}

    def logic(value, weight):
        if bag["weight"] + weight <= maxW:
            bag["value"] += value
            bag["weight"] += weight
        elif bag["value"] < value:
            bag["value"] = value

    if weight1 <= maxW:
        logic(value1, weight1)
    if weight2 <= maxW:
        logic(value2, weight2)

    return bag["value"]


# ================================================#
#     ^ my answer      ||  most voted answer v   #
# ================================================#


def knapsackLight(v1, w1, v2, w2, W):
    return max(int(w1 <= W) * v1, int(w2 <= W) * v2, int(w1 + w2 <= W) * (v1 + v2))

    # return max(v for v, w in ((0, 0), (v1, w1), (v2, w2), (v1+v2, w1+w2)) if w <= maxW)


# ================================================#
#                 question v                     #
# ================================================#

# You found two items in a treasure chest! The first item weighs weight1 and is worth value1, and the second item weighs weight2 and is worth value2. What is the total maximum value of the items you can take with you, assuming that your max weight capacity is maxW and you can't come back for the items later?

# Note that there are only two items and you can't bring more than one item of each type, i.e. you can't take two first items or two second items.

# Example

# For value1 = 10, weight1 = 5, value2 = 6, weight2 = 4, and maxW = 8, the output should be
# knapsackLight(value1, weight1, value2, weight2, maxW) = 10.

# You can only carry the first item.

# For value1 = 10, weight1 = 5, value2 = 6, weight2 = 4, and maxW = 9, the output should be
# knapsackLight(value1, weight1, value2, weight2, maxW) = 16.

# You're strong enough to take both of the items with you.

# For value1 = 5, weight1 = 3, value2 = 7, weight2 = 4, and maxW = 6, the output should be
# knapsackLight(value1, weight1, value2, weight2, maxW) = 7.

# You can't take both items, but you can take any of them.

# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] integer value1

# Guaranteed constraints:
# 2 ≤ value1 ≤ 20.

# [input] integer weight1

# Guaranteed constraints:
# 2 ≤ weight1 ≤ 10.

# [input] integer value2

# Guaranteed constraints:
# 2 ≤ value2 ≤ 20.

# [input] integer weight2

# Guaranteed constraints:
# 2 ≤ weight2 ≤ 10.

# [input] integer maxW

# Guaranteed constraints:
# 1 ≤ maxW ≤ 20.

# [output] integer

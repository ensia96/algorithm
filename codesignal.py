def longestDigitsPrefix(inputString):
    return "".join([_ if _.isdigit() else "_" for _ in inputString]).split("_")[0]


# ================================================#
#     ^ my answer      ||  most voted answer v   #
# ================================================#


def longestDigitsPrefix(inputString):
    return re.findall("^\d*", inputString)[0]


# ================================================#
#                 question v                     #
# ================================================#

# Given a string, output its longest prefix which contains only digits.

# Example

# For inputString = "123aa1", the output should be
# longestDigitsPrefix(inputString) = "123".

# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] string inputString

# Guaranteed constraints:
# 3 ≤ inputString.length ≤ 100.

# [output] string

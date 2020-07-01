def firstDigit(inputString):
    from string import digits

    return [i for i in inputString if i in digits][0]


# ================================================#
#     ^ my answer      ||  most voted answer v   #
# ================================================#


def firstDigit(inputString):
    for i in inputString:
        if i.isdigit():
            return i


# def firstDigit(inputString):
#     return re.findall('\d', inputString)[0]


# ================================================#
#                 question v                     #
# ================================================#

# Find the leftmost digit that occurs in a given string.

# Example

# For inputString = "var_1__Int", the output should be
# firstDigit(inputString) = '1';
# For inputString = "q2q-q", the output should be
# firstDigit(inputString) = '2';
# For inputString = "0ss", the output should be
# firstDigit(inputString) = '0'.
# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] string inputString

# A string containing at least one digit.

# Guaranteed constraints:
# 3 ≤ inputString.length ≤ 10.

# [output] char

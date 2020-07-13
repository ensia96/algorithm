def lineEncoding(s):
    s_list = [""]
    for _ in s:
        if _ not in s_list[-1]:
            s_list.append(_)
        else:
            s_list[-1] += _
    s_list.pop(0)
    return "".join(
        [str(_.count(_[0])) + _[0] if _.count(_[0]) != 1 else _ for _ in s_list]
    )


# ================================================#
#     ^ my answer      ||  most voted answer v   #
# ================================================#


def lineEncoding(s):
    return re.sub(r"(.)\1+", lambda m: str(len(m.group(0))) + m.group(1), s)


# def lineEncoding(s):
#     from itertools import groupby

#     x = ""
#     for k, g in groupby(s):
#         y = len((list(g)))
#         if y == 1:
#             x += k
#         else:
#             x += str(y) + k
#     return x


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

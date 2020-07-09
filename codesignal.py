def buildPalindrome(st):
    _st = st[::-1]
    answer = ""
    while True:
        palindrome = st + _st
        if palindrome == palindrome[::-1]:
            answer = palindrome
        if len(_st) == 0:
            return answer
        _st = _st[1:]


# ================================================#
#     ^ my answer      ||  most voted answer v   #
# ================================================#


def buildPalindrome(st):
    for i in range(0, len(st)):
        if st[i : len(st)] == st[i : len(st)][::-1]:
            return st[0:i] + st[i : len(st)] + st[0:i][::-1]


# ================================================#
#                 question v                     #
# ================================================#

# Given a string, find the shortest possible string which can be achieved by adding characters to the end of initial string to make it a palindrome.

# Example

# For st = "abcdc", the output should be
# buildPalindrome(st) = "abcdcba".

# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] string st

# A string consisting of lowercase English letters.

# Guaranteed constraints:
# 3 ≤ st.length ≤ 10.

# [output] string

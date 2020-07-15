class Solution:
    def checkValidString(self, s: str) -> bool:
        if s == "":
            return True
        i = 0
        for _ in s:
            if _ == "(":
                i += 1
            if _ == ")":
                i -= 1
            if _ == "*":
                if s.count("(") > s.count(")"):
                    i += 1
                if s.count("(") < s.count(")"):
                    i -= 1
            if i < 0:
                return False
        if i == 0:
            return True
        return False


#
#
#
#
# ================================================#
#     ^ my answer      ||  most voted answer v   #
# ================================================#


class Solution:
    def checkValidString(self, s: str) -> bool:
        cmin = cmax = 0
        for i in s:
            if i == "(":
                cmax += 1
                cmin += 1
            if i == ")":
                cmax -= 1
                cmin = max(cmin - 1, 0)
            if i == "*":
                cmax += 1
                cmin = max(cmin - 1, 0)
            if cmax < 0:
                return False
        return cmin == 0


class Solution:
    def checkValidString(self, s: str) -> bool:
        cmin = cmax = 0
        for i in s:
            cmax = cmax - 1 if i == ")" else cmax + 1
            cmin = cmin + 1 if i == "(" else max(cmin - 1, 0)
            if cmax < 0:
                return False
        return cmin == 0


# ================================================#
#                  question v                     #
# ================================================#

# 678. Valid Parenthesis String
# Medium

# Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
# An empty string is also valid.
# Example 1:
# Input: "()"
# Output: True
# Example 2:
# Input: "(*)"
# Output: True
# Example 3:
# Input: "(*))"
# Output: True
# Note:
# The string size will be in the range [1, 100].

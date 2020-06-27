class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        standard = {_: [] for _ in set(["".join(sorted(str)) for str in strs])}
        for str in strs:
            standard["".join(sorted(str))].append(str)
        return list(standard.values())


# Success
# Details
# Runtime: 108 ms, faster than 51.36% of Python3 online submissions for Group Anagrams.
# Memory Usage: 17 MB, less than 62.06% of Python3 online submissions for Group Anagrams.

# ================================================#
#     ^ my answer      ||  most voted answer v   #
# ================================================#


class Solution:
    def groupAnagrams(self, strs):
        d = {}
        for w in sorted(strs):
            key = tuple(sorted(w))
            d[key] = d.get(key, []) + [w]
        return d.values()


# ================================================#
#                 question v                     #
# ================================================#

# 49. Group Anagrams
# Medium

# Given an array of strings, group anagrams together.

# Example:

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:

# All inputs will be in lowercase.
# The order of your output does not matter.

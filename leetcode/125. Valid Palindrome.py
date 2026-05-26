class Solution:
    def isPalindrome(self, s: str) -> bool:
        return (i := ''.join(filter(str.isalnum, s)).lower()) == i[::-1]

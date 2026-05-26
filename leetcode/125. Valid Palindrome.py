class Solution:
    def isPalindrome(self, s: str) -> bool:
        return (i := ''.join(i.lower() for i in s if i.isalnum())) == i[::-1]

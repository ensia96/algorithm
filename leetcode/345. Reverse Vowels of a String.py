class Solution:
    def reverseVowels(self, s: str) -> str:
        D = 'aeiouAEIOU'
        A = [i for i in s if i in D]
        return ''.join(A.pop()if i in D else i for i in s)

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        a, b, c = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
        return [i for i in words if (l := set(i.lower())) <= a or l <= b or l <= c]

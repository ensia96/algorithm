class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        from itertools import repeat
        if len(words) == 1:
            return list(words[0])
        A = []
        for i in set(min(words, key=len)):
            if all(i in w for w in words):
                A.extend([i] * min(map(str.count, words, repeat(i))))
        return A

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        M = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
             "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        return len({''.join(M[ord(c) - 97] for c in w)for w in words})

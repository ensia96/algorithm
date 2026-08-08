class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        M = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        R = {s: M[i] if i < 3 else str(
            i + 1) for i, s in enumerate(sorted(score, reverse=True))}
        return [R[s] for s in score]

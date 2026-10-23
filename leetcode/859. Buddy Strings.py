class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            return len(set(s)) < len(s)
        return len(P := [(a, b)for a, b in zip(s, goal) if a != b]) == 2 and P[0] == P[1][::-1]

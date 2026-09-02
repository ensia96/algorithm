class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        m, A, D = float('inf'), [], {j: i for i, j in enumerate(list1)}
        for i, j in enumerate(list2):
            if j in D:
                x = i + D[j]
                if x < m:
                    m, A = x, []
                if x == m:
                    A.append(j)
        return A

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        A, D = [], {}
        for i in nums1:
            D[i] = D.get(i, 0) + 1
        for i in nums2:
            if D.get(i, 0) > 0:
                A += i,
                D[i] -= 1
        return A

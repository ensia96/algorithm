class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        S = []
        D = {}
        for i in nums2:
            while S and S[-1] < i:
                D[S.pop()] = i
            S.append(i)
        return [D.get(i, -1) for i in nums1]

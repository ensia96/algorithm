class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        f = 2
        return {(f := f * (i < j)) or i > j for i, j in zip(arr, arr[1:])} == {1, 2}

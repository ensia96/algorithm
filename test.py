class Solution:
    def findMaxLength(self, nums):
        if not nums:
            return 0
        while True:
            print(nums.count(0))
            print(nums.count(1))
            print("===================")
            if nums.count(0) == nums.count(1):
                return len(nums)
            if nums.count(0) > nums.count(1):
                if nums[0] == 0:
                    nums.pop(0)
                else:
                    nums.pop()
            elif nums.count(0) < nums.count(1):
                if nums[0] == 1:
                    nums.pop(0)
                else:
                    nums.pop()


a = Solution()
print(
    a.findMaxLength(
        [
            0,
            1,
            0,
            1,
            1,
            1,
            0,
            0,
            1,
            1,
            0,
            1,
            1,
            1,
            1,
            1,
            1,
            0,
            1,
            1,
            0,
            1,
            1,
            0,
            0,
            0,
            1,
            0,
            1,
            0,
            0,
            1,
            0,
            1,
            1,
            1,
            1,
            1,
            1,
            0,
            0,
            0,
            0,
            1,
            0,
            0,
            0,
            1,
            1,
            1,
            0,
            1,
            0,
            0,
            1,
            1,
            1,
            1,
            1,
            0,
            0,
            1,
            1,
            1,
            1,
            0,
            0,
            1,
            0,
            1,
            1,
            0,
            0,
            0,
            0,
            0,
            0,
            1,
            0,
            1,
            0,
            1,
            1,
            0,
            0,
            1,
            1,
            0,
            1,
            1,
            1,
            1,
            0,
            1,
            1,
            0,
            0,
            0,
            1,
            1,
        ]
    )
)

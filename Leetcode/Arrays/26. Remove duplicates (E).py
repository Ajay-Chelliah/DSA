class Solution:
    def removeDuplicates(self, nums) -> int:
        i = 0
        for j in range(i + 1, len(nums)):
            if nums[j] != nums[i]:
                nums[i + 1] = nums[j]
                i += 1
        return i + 1

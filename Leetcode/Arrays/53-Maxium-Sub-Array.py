class Solution:
    def maxSubArray(self, nums):
        max = float("-inf")
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                if sum > max:
                    max = sum
        return max

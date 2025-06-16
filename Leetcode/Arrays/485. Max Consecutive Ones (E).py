class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        c = 0
        list1 = []
        for i in range(len(nums)):
            if nums[i] == 1:
                c = c + 1
            else:
                list1.append(c)
                c = 0
        list1.append(c)
        return max(list1)

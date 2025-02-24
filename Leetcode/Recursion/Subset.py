class Solution:
    def subsetsWithDup(self, nums):
        ans = []
        res = set()

        def subset(i, list1):
            if i == len(nums):
                list1.sort()
                res.add(tuple(list1))
                return
            list1.append(nums[i])
            subset(i + 1, list1)
            list1.remove(nums[i])
            subset(i + 1, list1)

        subset(0, [])
        for it in res:
            ans.append(list(it))
        return ans

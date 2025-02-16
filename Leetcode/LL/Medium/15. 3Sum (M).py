class Solution:
    def threeSum(self, nums):
        list1 = sorted(nums)
        list2 = []
        leng = len(nums)
        for i in range(len(list1)):
            if i > 0 and list1[i] == list1[i - 1]:
                continue
            j = i + 1
            k = leng - 1
            while j < k:
                sum = list1[i] + list1[j] + list1[k]
                if sum < 0:
                    j += 1
                if sum > 0:
                    k -= 1
                if sum == 0:
                    list2.append([list1[i], list1[j], list1[k]])
                    j += 1
                    k -= 1
                    while j < k and list1[j] == list1[j - 1]:
                        j += 1
                    while j < k and list1[k] == list1[k + 1]:
                        k -= 1
        return list2

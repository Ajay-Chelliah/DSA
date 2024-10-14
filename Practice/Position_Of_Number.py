"""
Question: Given an array of integers nums sorted in ascending order,
          find the starting and ending position of a given number.

Idea    : Binary Search

Example :
        arr = [2,4,6,6,8,10]
        num = 6

Output :
        [3,4]

"""
# Code :

import time

start_time = time.time()


class Solution:
    @staticmethod
    def binary_Search(arr, num, val):
        c = True
        start = 0
        end = len(arr) - 1
        while start <= end:
            mid = (start + end) // 2
            if arr[mid] == num:
                if val:
                    if mid - 1 >= 0 and arr[mid - 1] == arr[mid]:
                        end = mid - 1
                    else:
                        return mid
                else:
                    if mid + 1 < len(arr) and arr[mid + 1] == arr[mid]:
                        start = mid + 1
                    else:
                        return mid

            elif arr[mid] < num:
                start = mid + 1
            elif arr[mid] > num:
                end = mid - 1
        return -1

    def searchRange(self, nums, target: int):
        first = Solution.binary_Search(nums, target, True)
        last = Solution.binary_Search(nums, target, False)
        return [first, last]


obj = Solution()
nums = [2, 2]
target = 2
print(obj.searchRange(nums, target))
end_time = time.time()
execution_time = (end_time - start_time) * 1000
print(f"Execution time: {execution_time:.2f} ms")

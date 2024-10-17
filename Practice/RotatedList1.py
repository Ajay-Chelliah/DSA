"""
Problem : Need to find the position of an element in the array
          which is formed after number of repetations on a sorted array.

Idea : Binary Search

Input : Array , element

Output : Position
"""


# Code :
def search_rotated_sorted_array(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


# Example
rotated_list = [5, 6, 9, 0, 2, 3, 4]
target_number = 2
position = search_rotated_sorted_array(rotated_list, target_number)
print(position)

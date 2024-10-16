"""
Problem : We are having two list, second list is the first list after few rotations.
          We need to find the number of rotations made

Idea : Binary Search

Input   : Two Lists

Output   : Number of Rotations.

Note : I have tried three ways
    Time complexity of,
        First : n(log n) ---> Sorting and Binary Search
        Second : n       ---> Linear Search
        Thrid : log n    ---> Binary Search

Result : All the test cases has been passed for all the three codes.
"""

# Code :
from jovian.pythondsa import evaluate_test_cases
from jovian.pythondsa import evaluate_test_case

# Edge cases
test0 = {"input": {"nums": [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]}, "output": 3}

test1 = {"input": {"nums": [5, 6, 7, 8, 1, 2, 3, 4]}, "output": 4}

# A list that wasn't rotated at all.
test2 = {"input": {"nums": [1, 2, 3, 4, 5, 6, 7, 8]}, "output": 0}

# A list that was rotated just once.
test3 = {"input": {"nums": [8, 1, 2, 3, 4, 5, 6, 7]}, "output": 1}

# A list that was rotated n-1 times, where n is the size of the list.
test4 = {"input": {"nums": [2, 3, 4, 5, 6, 7, 8, 1]}, "output": 7}

# A list that was rotated n times (do you get back the original list here?)
test5 = {"input": {"nums": [1, 2, 3, 4, 5, 6, 7, 8]}, "output": 0}

# An empty list.
test6 = {"input": {"nums": []}, "output": None}

# A list containing just one element.
test7 = {"input": {"nums": [1]}, "output": 0}

tests = [test0, test1, test2, test3, test4, test5, test6, test7]


# Code 1 :
def binary_search(arr, ele):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == ele:
            return mid
        elif arr[mid] > ele:
            end = mid - 1
        elif arr[mid] < ele:
            start = mid + 1
    return -1


def count_rotations(nums):
    if len(nums) == 0:
        return None
    arr1 = sorted(nums)
    end = len(arr1) - 1
    mid = (0 + end) // 2
    val = nums[mid]
    pos = binary_search(arr1, val)
    if pos > mid:
        return len(arr1) - (pos - mid)
    else:
        return mid - pos


evaluate_test_cases(count_rotations, tests)
evaluate_test_case(count_rotations, test0)


# Code 2 :
def count_linear(nums):
    if len(nums) == 0:
        return None
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            return i
    return 0


evaluate_test_case(count_linear, test0)
evaluate_test_cases(count_linear, tests)


# Code 3:
def count_binary(nums):
    if len(nums) == 0:
        return None
    leng = len(nums)
    start = 0
    end = leng - 1
    while start < end:
        mid = (start + end) // 2
        if nums[mid] < nums[mid - 1]:
            return mid
        elif nums[mid] < nums[leng - 1]:
            end = mid - 1
        elif nums[mid] > nums[leng - 1]:
            start = mid + 1
    return (start + end) // 2


evaluate_test_case(count_binary, test0)
evaluate_test_cases(count_binary, tests)

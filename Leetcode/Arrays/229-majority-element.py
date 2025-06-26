def majorityElement(nums):
    list1 = []
    dict1 = {}
    n = len(nums)
    for i in nums:
        if i in dict1:
            dict1[i] += 1
            continue
        dict1[i] = 1
    for i, j in dict1.items():
        if j > (n // 3):
            list1.append(i)
    return list1

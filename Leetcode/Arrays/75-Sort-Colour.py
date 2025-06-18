def sortColors(nums) -> None:
    a = nums.count(0)
    b = nums.count(1)
    c = nums.count(2)
    s = "0" * a + "1" * b + "2" * c
    k = 0
    for i in s:
        nums[k] = int(i)
        k += 1
    print(nums)

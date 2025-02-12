# Insertion sort

arr = [13, 46, 24, 52, 20, 9]
for i in range(len(arr)):
    min = arr[i]
    for j in range(i, len(arr)):
        if arr[j] < min:
            min = arr[j]
            ind = j
    temp = arr[i]
    arr[i] = min
    arr[ind] = temp
    print(arr)

# Bubble sort
arr = [13, 46, 24, 52, 20, 9]
for i in range(len(arr) - 1):
    for j in range(len(arr) - i - 1):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp
    print(arr)

# Selection sort
arr = [14, 9, 15, 12, 6, 8, 13]

for i in range(len(arr)):
    j = i
    while j > 0 and arr[j] < arr[j - 1]:
        temp = arr[j]
        arr[j] = arr[j - 1]
        arr[j - 1] = temp
        j -= 1
        # print(arr)
    print(arr)

# Merge sort

arr = [3, 2, 4, 1, 3]
temp = []
leng = len(arr)


def merge_divide(arr, low, high):
    if low == high:
        return
    mid = (low + high) // 2
    merge_divide(arr, low, mid)
    merge_divide(arr, mid + 1, high)
    merge(arr, low, mid, high)


def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    while left <= mid:
        temp.append(arr[left])
        left += 1
    while right <= high:
        temp.append(arr[right])
        right += 1
    for i in range(len(temp)):
        arr[low + i] = temp[i]
        print(arr)


merge_divide(arr, 0, leng - 1)


# Quick sort

arr = [4, 6, 2, 5, 7, 9, 1, 3]


def quick_sort(arr, low, high):
    if low < high:
        pivot = find_pivot(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)
    print(arr)


def find_pivot(arr, low, high):
    pivot = arr[low]
    i = low
    j = high
    while i < j:
        while arr[i] <= pivot and i < high:
            i += 1
        while arr[j] > pivot and j > low:
            j -= 1
        if i < j:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    temp = arr[low]
    arr[low] = arr[j]
    arr[j] = temp
    return j


quick_sort(arr, 0, len(arr) - 1)

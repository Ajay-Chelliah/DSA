import time

ele = 4
ele1 = 5
arr = [5, 1, 2, 3, 4]
arr1 = [1, 2, 3, 4, 5]


def linearSearch(arr, ele):
    # print("**LinearSearch**")
    start_time = time.perf_counter()
    for i in range(len(arr)):
        if arr[i] == ele:
            print(i)
            end_time = time.perf_counter()
            print(end_time - start_time)
            break


linearSearch(arr1, ele1)


def binarySearch(arr, ele):
    # print("**BinarySearch**")
    start_time = time.perf_counter()
    arr = sorted(arr)
    # print(arr)
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > ele:
            high = mid - 1
        if arr[mid] < ele:
            low = mid + 1
        if arr[mid] == ele:
            print(mid)
            end_time = time.perf_counter()
            print(end_time - start_time)
            break


binarySearch(arr1, ele1)


def binary_recursion(arr, ele, low, high):
    if low > high:
        return
    mid = (low + high) // 2
    if arr[mid] < ele:
        binary_recursion(arr, ele, mid + 1, high)
    if arr[mid] > ele:
        binary_recursion(arr, ele, low, mid - 1)
    if arr[mid] == ele:
        print(mid)
        return


start_time = time.perf_counter()
binary_recursion(arr, ele, 0, len(arr) - 1)
end_time = time.perf_counter()
print(end_time - start_time)

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

arr = [5, 4, 3, 2, 1]


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    print(arr)


bubble_sort(arr)


def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp
    print(arr)


selection_sort(arr)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j] < arr[j - 1]:
            temp = arr[j]
            arr[j] = arr[j - 1]
            arr[j - 1] = temp
            j -= 1
    print(arr)


insertion_sort(arr)

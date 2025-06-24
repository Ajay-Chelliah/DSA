def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    m = len(matrix)
    n = len(matrix[0])
    for i in matrix:
        if target <= i[n - 1]:
            low = 0
            high = n - 1
            while low <= high:
                mid = (low + high) // 2
                if i[mid] == target:
                    return True
                elif i[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return False
    return False

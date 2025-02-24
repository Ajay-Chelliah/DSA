class Solution:
    def __init__(self):
        self.list1 = []

    def subsetSums(self, arr):
        self.recur(arr, 0, 0)
        return self.list1

    def recur(self, arr, i, currentSum):
        if i == len(arr):
            self.list1.append(currentSum)
            return
        self.recur(arr, i + 1, currentSum + arr[i])
        self.recur(arr, i + 1, currentSum)

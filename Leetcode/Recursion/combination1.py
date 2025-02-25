from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        list1 = []
        ds = []

        def recur(i, target):
            if i == len(candidates):
                if target == 0:
                    list1.append(ds[:])
                return
            if candidates[i] <= target:
                ds.append(candidates[i])
                recur(i, target - candidates[i])
                ds.pop()
            recur(i + 1, target)

        recur(0, target)
        return list1

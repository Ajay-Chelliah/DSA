class Solution:
    # Function to find the minimum number of platforms required at the
    # railway station such that no train waits.
    def minimumPlatform(self, arr, dep):
        arr.sort()
        dep.sort()
        leng = len(arr)
        i, c = 0, 0
        j = 0
        maxi = 0
        while i < leng:
            if arr[i] <= dep[j]:
                c += 1
                i += 1
            else:
                c -= 1
                j += 1
            maxi = max(maxi, c)
        return maxi

class Solution:
    def firstIndex(self, arr, n):
        left = 0
        right = n-1
        result = -1
        while left <= right:
            mid = left + (right - left)//2
            if arr[mid] == 1:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        return result
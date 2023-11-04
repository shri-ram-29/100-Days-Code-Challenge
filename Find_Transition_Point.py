class Solution:
    def transitionPoint(self, arr, n):
        if 1 not in arr:
            return -1
        if 0 not in arr:
            return 0
        low, high = 0, n - 1
        while low <= high:
            mid = low + (high - low) // 2 
            if arr[mid] == 1 and arr[mid - 1] == 0:
                return mid 
            if arr[mid] == 0:
                low = mid + 1
            else:
                high = mid - 1
        return -1
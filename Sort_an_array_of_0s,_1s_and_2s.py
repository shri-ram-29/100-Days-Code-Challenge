class Solution:
    def sort012(self,arr,n):
        size = len(arr)
        low,high,mid = 0, size-1,0
        while mid<=high:
            if arr[mid]==0:
                arr[low],arr[mid] = arr[mid],arr[low]
                low = low + 1
                mid = mid + 1
            elif arr[mid] == 1:
                mid = mid + 1
            else:
                arr[mid],arr[high] = arr[high],arr[mid]
                high = high - 1
        return arr
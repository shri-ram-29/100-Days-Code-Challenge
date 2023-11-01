class Solution:
    def duplicates(self, arr, n): 
        result = []
        for i in range(n):
            index = arr[i] % n
            if arr[index] >= n:
                if arr[index] < 2 * n:
                    result.append(index)
            arr[index] += n

        if not result:
            return [-1]
        else:
            return sorted(result)
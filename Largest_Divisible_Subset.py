class Solution:
    def largestDivisibleSubset(self, nums):
        if not nums:
            return []

        nums.sort()
        n = len(nums)
        dp = [1] * n
        prev = [-1] * n
        max_len, max_idx = 1, 0

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j
                    if dp[i] > max_len:
                        max_len, max_idx = dp[i], i

        result = []
        while max_idx != -1:
            result.append(nums[max_idx])
            max_idx = prev[max_idx]

        return result[::-1]
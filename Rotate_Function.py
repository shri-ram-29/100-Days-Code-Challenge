class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        sum_nums = sum(nums)
        curr_sum = sum(i * nums[i] for i in range(n))
        max_sum = curr_sum

        for k in range(1, n):
            curr_sum += sum_nums - n * nums[n - k]
            max_sum = max(max_sum, curr_sum)

        return max_sum

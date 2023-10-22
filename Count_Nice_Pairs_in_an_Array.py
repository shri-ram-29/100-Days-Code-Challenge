class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        def reverse_num(x):
            return int(str(x)[::-1])

        reversed_nums = [reverse_num(x) for x in nums]
        num_counts = {}
        nice_pairs = 0

        for i in range(len(nums)):
            diff = nums[i] - reversed_nums[i]
            if diff in num_counts:
                nice_pairs += num_counts[diff]
                num_counts[diff] += 1
            else:
                num_counts[diff] = 1

        return nice_pairs % MOD

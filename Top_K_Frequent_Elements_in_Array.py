class Solution:
    def topK(self, nums, k):
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        topk = sorted(freq.items(), key=lambda x: (-x[1], -x[0]))
        return [topk[i][0] for i in range(k)]
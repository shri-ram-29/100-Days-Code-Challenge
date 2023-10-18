from collections import Counter, defaultdict
from typing import List

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        count = Counter(nums)
        end = defaultdict(int)

        for num in nums:
            if count[num] == 0:
                continue
            count[num] -= 1
            if end[num - 1] > 0:
                end[num - 1] -= 1
                end[num] += 1
            elif count[num + 1] > 0 and count[num + 2] > 0:
                count[num + 1] -= 1
                count[num + 2] -= 1
                end[num + 2] += 1
            else:
                return False

        return True

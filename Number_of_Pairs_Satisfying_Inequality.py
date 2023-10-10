from sortedcontainers import SortedList

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        sl, ans = SortedList(), 0
        
        for num1, num2 in zip(nums1, nums2):
            current_diff = num1 - num2
            ans += sl.bisect_right(current_diff + diff)
            sl.add(current_diff)
        
        return ans

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        counts = [0, 0, 0]
        left = 0 
        result = 0
        
        for right in range(len(s)):
            counts[ord(s[right]) - ord('a')] += 1
            while all(counts):
                result += len(s) - right
                counts[ord(s[left]) - ord('a')] -= 1
                left += 1
        
        return result

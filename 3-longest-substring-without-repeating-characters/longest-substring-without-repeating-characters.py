class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap = {}
        left = 0
        max_count = 0
        for right in range(len(s)):
            c = s[right]
            if c in charMap and charMap[c] >= left:
                left = charMap[c] + 1
            charMap[c] = right
            max_count = max(max_count, (right-left) + 1)
            #if max_count < (right - left) + 1:
            #    max_count = (right - left) + 1
        return max_count

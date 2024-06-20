class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        indexes = {}
        from_i = 0
        max_count = 0
        for i in range(len(s)):
            c = s[i]
            if c in indexes and indexes[c] >= from_i:
                from_i = indexes[c] + 1
            indexes[c] = i
            if max_count < (i - from_i) + 1:
                max_count = (i - from_i) + 1
        return max_count

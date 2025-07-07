class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        seen = set()
        for n in nums:
            if n not in seen:
                seen.add(n)
                nums[i] = n
                i += 1
        return len(seen)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        maxn = None
        maxv = 0
        for n in nums:
            if n not in count:
                count[n] = 0
            count[n] += 1
            if count[n] > maxv:
                maxn = n
                maxv = count[n]
        return maxn

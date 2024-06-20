class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = set(nums)
        k = len(s)
        nums[:] = sorted(list(s))
        return k



        

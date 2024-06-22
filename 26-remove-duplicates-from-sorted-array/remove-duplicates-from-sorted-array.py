class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        len_arr = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[len_arr] = nums[i]
                len_arr += 1
        return len_arr

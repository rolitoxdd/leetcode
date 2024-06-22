class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start, end = 0,len(nums) - 1
        while start <= end:
            if nums[end] == val:
                end -= 1
                continue
            if nums[start] == val:
                nums[start] = nums[end]
                end -= 1
            start += 1

        return end + 1


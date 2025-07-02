class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if nums[-1] - nums[0] > 0:
            direction = 1
        else:
            direction = -1
    
        for i in range(1, len(nums)):
            sign = nums[i] - nums[i - 1]
            if sign > 0:
                sign = 1
            elif sign < 0:
                sign = -1
            else:
                sign = 0
            
            if sign and direction != sign:
                return False
        return True
                
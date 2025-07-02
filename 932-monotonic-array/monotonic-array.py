class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        direction = 0
        for i in range(1, len(nums)):
            sign = nums[i] - nums[i - 1]
            if sign > 0:
                sign = 1
            elif sign < 0:
                sign = -1
            else:
                sign = 0
            if not direction:
                direction = sign
            
            if sign and direction != sign:
                return False
        return True
                
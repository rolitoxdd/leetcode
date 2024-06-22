class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = []
        for i in range(len(nums)):
            j = len(nums) - 1 - i
            if i == 0:
                left_multiplication = 1
            else:
                left_multiplication = nums[i-1] * left_multiplication
            if j == len(nums) - 1:
                right_multiplication = 1
            else:
                right_multiplication = nums[j+1] * right_multiplication
            left.append(left_multiplication)
            right.append(right_multiplication)
        res = []
        for i in range(len(nums)):
            res.append(left[i] * right[len(nums) - 1 - i])
        return res

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = []
        n = len(nums)
        left_multiplication = 1
        right_multiplication = 1
        for i in range(n):
            j = n - 1 - i
            if i != 0:
                left_multiplication = nums[i-1] * left_multiplication
            if j != n - 1:
                right_multiplication = nums[j+1] * right_multiplication
            left.append(left_multiplication)
            right.append(right_multiplication)
        return [left[i] * right[n-i-1] for i in range(n)]

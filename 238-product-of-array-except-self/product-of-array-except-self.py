class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        prefix = 1
        suffix = 1
        for i in range(len(nums)):
            answer[i] = answer[i] * prefix
            answer[-i-1] = answer[-i-1] * suffix 
            prefix *= nums[i]
            suffix *= nums[-i-1]
        return answer
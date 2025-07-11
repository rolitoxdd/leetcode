class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.solution2(nums, k)
    
    def solution1(self, nums: List[int], k: int) -> None:
        for _ in range(k):
            aux = nums[0]
            for i in range(len(nums)):
                aux2 = nums[(i+1) % len(nums)]
                nums[(i+1)% len(nums)] = aux
                aux = aux2

    def solution2(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        

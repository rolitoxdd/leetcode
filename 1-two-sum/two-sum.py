class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            n = nums[i]
            if n in d:
                d[n].append(i)
            else:
                d[n] = [i]
        
        for k in d:
            complement = target - k
            if complement != k and complement in d:
                return [d[k][0], d[complement][0]]
            elif complement == k and len(d[k]) >= 2:
                return [d[k][0], d[k][1]]
        

            
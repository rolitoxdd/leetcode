class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        l = len(nums)
        if l == 1:
            return nums
        half = self.sortArray(nums[:l//2])
        half_2 = self.sortArray(nums[l//2:])

        i = 0
        j = 0
        res = []
        while i != len(half) and j != len(half_2):
            if half[i] < half_2[j]:
                res.append(half[i])
                i+=1
            else:
                res.append(half_2[j])
                j+=1
        while i != len(half):
            res.append(half[i])
            i+=1
        while j != len(half_2):
            res.append(half_2[j])
            j+=1
        return res 
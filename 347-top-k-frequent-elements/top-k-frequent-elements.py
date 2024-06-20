class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1
        d = sorted(d.items(), key= lambda x: x[1], reverse=True)
        res = []
        for i in range(k):
            res.append(d[i][0])
        return res


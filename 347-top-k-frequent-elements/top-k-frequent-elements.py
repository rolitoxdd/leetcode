class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for n in nums:
            freqs[n] = freqs.get(n, 0) + 1
        
        order = [[] for _ in range(len(nums))]

        for n in freqs:
            f = freqs[n]
            order[f - 1].append(n)
        
        res = []
        while k:
            l = order.pop()
            if not l:
                continue
            res.append(l.pop())
            k -= 1
            if l:
                order.append(l)
        return res

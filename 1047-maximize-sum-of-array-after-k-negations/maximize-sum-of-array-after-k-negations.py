import queue
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        pq = queue.PriorityQueue()
        for i in range(len(nums)):
            pq.put((nums[i], i))
        for _ in range(k):
            x = pq.get()
            pq.put((-1*x[0], x[1]))
        
        sum = 0
        while not pq.empty():
            v = pq.get()
            sum += v[0]
        return sum
        

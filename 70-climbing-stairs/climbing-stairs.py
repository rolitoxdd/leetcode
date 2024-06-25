class Solution:
    cache = {}
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        if n - 1 not in self.cache:
            self.cache[n - 1] = self.climbStairs(n - 1)
        if n - 2 not in self.cache:
            self.cache[n - 2] = self.climbStairs(n - 2)

        one_step = self.cache[n - 1]
        two_steps = self.cache[n - 2]

        return one_step + two_steps
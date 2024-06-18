class Solution:
    def largestInteger(self, num: int) -> int:
        digits = [int(n) for n in str(num)]
        evens = sorted([d for d in digits if d % 2 == 0])
        odds = sorted([d for d in digits if d % 2 != 0])
        are_evens = [True if d % 2 == 0 else False for d in digits]
        new_num = 0
        for is_even in are_evens:
            new_num *= 10
            if is_even:
                new_num += evens.pop()
            else:
                new_num += odds.pop()
        return new_num

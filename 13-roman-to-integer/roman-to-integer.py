class Solution:
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    def romanToInt(self, s: str) -> int:
        v = 0
        last_value = 0
        for c in s:
            n = self.values[c]
            if last_value < n:
                v += (n - last_value * 2)
            else:
                v += n
            last_value = n
        return v            
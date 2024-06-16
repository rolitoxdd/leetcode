class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        x = []
        for i in range(1, n + 1):
            res = ""
            if i % 3 == 0:
                res += "Fizz"
            if i % 5 == 0:
                res += "Buzz"
            if not res:
                res += str(i)
            x.append(res)
        return x
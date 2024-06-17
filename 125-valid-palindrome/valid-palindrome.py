class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
        s = ''.join((c.lower() for c in s if c in letters))
        i = 0
        j = len(s) - 1
        while i<j:
            if s[i] != s[j]:
                return False
            i+=1
            j-=1
        else:
            return True        
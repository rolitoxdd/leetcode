class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        start = 0
        for w in words:
            if start == len(s):
                break
            if s[start:].startswith(w):
                start += len(w)
            else:
                return False
        if start == len (s):
            return True
        return False
            
        
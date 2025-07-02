class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word = ""
        new_word = True
        for c in s:
            if c != " " and new_word:
                last_word = c
                new_word = False
            elif c != " ":
                last_word += c
            else:
                new_word = True
        return len(last_word)
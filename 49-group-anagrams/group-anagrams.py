class Solution:
    

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for w in strs:
            letter_count = {}
            for c in w:
                if c in letter_count:
                    letter_count[c]+=1
                else:
                    letter_count[c] = 1
            str_items = sorted([f"{item[0]}{item[1]}" for item in letter_count.items()])
            key = ''.join(str_items)
            if key in groups:
                groups[key].append(w)
            else:
                groups[key] = [w]
        return groups.values()

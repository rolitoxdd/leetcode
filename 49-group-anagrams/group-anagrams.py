class Solution:
    

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for w in strs:
            sorted_w = ''.join(sorted(w))
            if sorted_w not in groups:
                groups[sorted_w] = []
            groups[sorted_w].append(w)

        return groups.values()

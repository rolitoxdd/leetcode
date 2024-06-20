class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        pair_count = {}
        counter = 0
        for pair in dominoes:
            pair.sort()
            str_pair = f"{pair[0]}{pair[1]}"
            if str_pair not in pair_count:
                pair_count[str_pair] = 1
            else:
                counter += pair_count[str_pair]
                pair_count[str_pair] += 1
        return counter


        
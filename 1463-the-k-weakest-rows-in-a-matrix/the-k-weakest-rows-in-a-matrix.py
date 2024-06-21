class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        x = []
        for i in range(len(mat)):
            row_count = mat[i].count(1)
            x.append((i, row_count))
        x.sort(key= lambda p: p[1])
        return [p[0] for p in x[:k]]
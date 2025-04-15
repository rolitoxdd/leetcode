class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {i: set() for i in range(9)}
        columns = {i: set() for i in range(9)}
        sub_boxes = {(i,j): set() for i in range(3) for j in range(3)}
        for i in range(len(board)):
            row = board[i]
            for j in range(len(row)):
                cell = row[j]
                if cell == '.':
                    continue
                if cell in rows[i]:
                    return False
                if cell in columns[j]:
                    return False
                rows[i].add(cell)
                columns[j].add(cell)
                x = i // 3
                y = j // 3
                if cell in sub_boxes[(x,y)]:
                    return False
                sub_boxes[(x,y)].add(cell)




        return True

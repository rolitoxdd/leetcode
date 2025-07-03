class Solution:
    def judgeCircle(self, moves: str) -> bool:
        position = [0,0]
        movements = {
            'U':(0,1),
            'D': (0,-1),
            'R': (1,0),
            'L': (-1,0)
        }
        for m in moves:
            change = movements[m]
            position[0] += change[0]
            position[1] += change[1]
        return position == [0,0]
from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stud = deque(students) # will use it like a queue
        sdwc = deque(sandwiches) # will use it like a stack

        counter = 0
        while len(stud) != counter:
            student = stud.popleft()
            sandwich = sdwc[0]
            if student == sandwich:
                sdwc.popleft()
                counter = 0
            else:
                stud.append(student)
                counter+=1
        return counter

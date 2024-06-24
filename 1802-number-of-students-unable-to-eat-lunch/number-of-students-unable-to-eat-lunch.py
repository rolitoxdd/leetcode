from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        st = deque(students) # will use it like a queue
        sa = deque(sandwiches) # will use it like a stack
        counter = 0
        while len(st) != counter:
            student = st.popleft()
            sandwich = sa[0]
            if student == sandwich:
                sa.popleft()
                counter = 0
            else:
                st.append(student)
                counter+=1
        return counter

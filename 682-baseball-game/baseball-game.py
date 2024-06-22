class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []
        for op in operations:
            if op == '+':
                records.append(records[-1] + records[-2])
            elif op == 'D':
                records.append(2 * records[-1])
            elif op == 'C':
                records.pop()
            else:
                records.append(int(op))
        return sum(records)
        
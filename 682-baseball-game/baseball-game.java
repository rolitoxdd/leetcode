import java.util.Stack;

class Solution {
    public int calPoints(String[] operations) {
        Stack<Integer> s = new Stack<>();
        for (int i = 0; i < operations.length; i++) {
            String op = operations[i];
            if (op.equals("+")) {
                int last = s.pop();
                int prev = s.peek();
                int sum = last + prev;
                s.push(last);
                s.push(sum);
            } else if (op.equals("D")) {
                int last = s.peek();
                s.push(2 * last);
            } else if (op.equals("C")) {
                s.pop();
            } else {
                int x = Integer.valueOf(op);
                s.push(x);
            }
        }
        int sum = 0;
        while (!s.empty()) {
            sum += s.pop();
        }
        return sum;
    }
}
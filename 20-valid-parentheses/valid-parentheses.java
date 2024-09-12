import java.util.Stack;
        
class Solution {
    public boolean isValid(String s) {
        Stack<Character> x = new Stack<>();
        for (int i=0; i<s.length(); i++){
            char c = s.charAt(i);
            if (c == '(' || c == '[' || c == '{') {
                x.push(c);
            } else if (x.isEmpty()) {
                return false; 
            } else if (c == ')' && x.peek() != '(') {
                return false;
            } else if (c == ']' && x.peek() != '[') {
                return false;
            } else if (c == '}' && x.peek() != '{') {
                return false;
            } else {
                x.pop();
            }
        }
        return x.isEmpty();
    }
}
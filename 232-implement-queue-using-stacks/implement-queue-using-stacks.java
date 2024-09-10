import java.util.Stack;

class MyQueue {

    Stack<Integer> s;
    Stack<Integer> aux;
    public MyQueue() {
        s = new Stack<>();
        aux = new Stack<>();
    }
    
    public void push(int x) {
        while (!s.empty()) {
            aux.push(s.pop());
        }
        s.push(x);
        while(!aux.empty()) {
            s.push(aux.pop());
        }
    }
    
    public int pop() {
        return s.pop();
    }
    
    public int peek() {
        return s.peek();
    }
    
    public boolean empty() {
        return s.empty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */
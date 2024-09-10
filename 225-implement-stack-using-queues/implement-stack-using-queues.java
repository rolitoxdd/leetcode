import java.util.Queue;
import java.util.LinkedList;

class MyStack {
    Queue<Integer> q;
    Queue<Integer> aux;

    public MyStack() {
        q = new LinkedList<>();
        aux = new LinkedList<>();
    }
    
    public void push(int x) {
        while (!q.isEmpty()) {
            aux.add(q.poll());
        }
        q.add(x);
        while (!aux.isEmpty()) {
            q.add(aux.poll());
        }
    }
    
    public int pop() {
        return q.poll();
    }
    
    public int top() {
        return q.peek();
    }
    
    public boolean empty() {
        return q.isEmpty();
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */
import java.util.PriorityQueue;
import java.util.HashMap;

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> f = new HashMap<>();
        for (int n : nums) {
            if (!f.containsKey(n)) {
                f.put(n, 0);
            }
            f.put(n,f.get(n) + 1);
        }

        PriorityQueue<Integer> pq = new PriorityQueue<>((a,b) -> f.get(b) - f.get(a));
        for (int key: f.keySet()) {
            pq.add(key);
        }

        int[] res = new int[k];
        for (int i = 0; i < k; i++) {
            res[i] = pq.poll();
        }

        return res;
    }
}
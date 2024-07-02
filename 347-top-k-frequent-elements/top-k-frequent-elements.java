import java.util.*;
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> h = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int n = nums[i];
            if (!h.containsKey(n)) {
                h.put(n, 0);
            }
            h.put(n, h.get(n) + 1);
        }

        PriorityQueue<Integer> pq = new PriorityQueue<>((a,b) -> h.get(b) - h.get(a));
        for (Integer key : h.keySet()) {
            pq.add(key);
        }

        int[] res = new int[k];
        for (int i=0; i<k; i++) {
            res[i] = pq.poll();
        }
        return res;

    }
}
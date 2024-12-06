import java.util.PriorityQueue;
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int i = 0; i < lists.length; i++) {
            ListNode l = lists[i];
            while (l != null) {
                pq.add(l.val);
                l = l.next;
            }
        }
        ListNode res = new ListNode();
        ListNode curr = res;
        while (!pq.isEmpty()) {
            curr.next = new ListNode();
            curr = curr.next;
            curr.val = pq.poll();
        }
        return res.next;
    }
}
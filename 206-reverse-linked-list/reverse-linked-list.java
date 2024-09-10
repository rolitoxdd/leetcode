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
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode actual = head;
        ListNode next = head == null ? null : head.next;
        while (actual != null) {
            actual.next = prev;
            prev = actual;
            actual = next;
            next = next == null ? null : next.next;
        }
        return prev;
    }
}
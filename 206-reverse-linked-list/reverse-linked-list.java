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
        ListNode next = null;
        if (actual != null) {
            next = actual.next;
        }
        while(actual != null) {
            actual.next = prev;
            prev = actual;
            actual = next;
            if (next != null) {
                next = next.next;
            } else {
                next = null;
            }
        }
        return prev;
    }
}
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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummyHead = new ListNode();
        ListNode aux = dummyHead;
        int carry = 0;
        while (l1 != null || l2 != null) {
            int a = 0;
            if (l1 != null) {
                a = l1.val;
                l1 = l1.next;
            }
            int b = 0;
            if (l2 != null) {
                b = l2.val;
                l2 = l2.next;
            }
            int c = a + b + carry;
            carry = c / 10;
            int val = c % 10;
            aux.next = new ListNode(val);
            aux = aux.next;
        }
        if (carry != 0) {
            aux.next = new ListNode(carry);
        }
        return dummyHead.next;
    }
}
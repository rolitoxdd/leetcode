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
        int carry = 0;
        ListNode head = new ListNode();
        ListNode l3 = head;
        while ( l1 != null || l2 != null) {
            l3.next = new ListNode();
            l3 = l3.next;
            int a, b;
            if (l1 == null) {
                a = 0;
            } else {
                a = l1.val;
                l1 = l1.next;
            }
            if (l2 == null) {
                b = 0;
            } else {
                b = l2.val;
                l2 = l2.next;
            }
            int sum = a + b + carry;
            carry = sum / 10;
            sum = sum % 10;
            l3.val = sum;
        }
        if (carry != 0) {
            l3.next = new ListNode(carry);
        }
        return head.next;
    }
}
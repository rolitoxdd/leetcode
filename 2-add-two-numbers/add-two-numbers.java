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
        ListNode l3head = new ListNode();
        ListNode current = l3head;
        int carry = 0;
        while (l1 != null || l2 != null) {

            int val1 = 0;
            int val2 = 0;
            current.next = new ListNode();
            current = current.next;
            if (l1 != null) {
                val1 = l1.val;
                l1 = l1.next;
            }
            if (l2 != null) {
                val2 = l2.val;
                l2 = l2.next;
            }

            int val3 = val1 + val2 + carry;

            if (val3 >= 10) {
                carry = 1;
            } else {
                carry = 0;
            }
            val3 = val3 % 10;
            current.val = val3;

        }
        if (carry == 1) {
            current.next = new ListNode(carry);
        }
        return l3head.next;
    }
}
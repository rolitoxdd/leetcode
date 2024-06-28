# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        elif len(lists) == 2:
            current0 = lists[0]
            current1 = lists[1]
            dummy_head = ListNode()
            current_res = dummy_head
            while current0 != None and current1 != None:
                if current0.val < current1.val:
                    current_res.next = ListNode(current0.val)
                    current0 = current0.next
                    current_res = current_res.next
                else:
                    current_res.next = ListNode(current1.val)
                    current1 = current1.next
                    current_res = current_res.next
            while current0 != None:
                current_res.next = ListNode(current0.val)
                current0 = current0.next
                current_res = current_res.next
            while current1 != None:
                current_res.next = ListNode(current1.val)
                current1 = current1.next
                current_res = current_res.next
            return dummy_head.next
                
        else:
            return self.mergeKLists(
                [
                    self.mergeKLists(lists[:len(lists)//2]), 
                    self.mergeKLists(lists[len(lists)//2:])
                ]
            )



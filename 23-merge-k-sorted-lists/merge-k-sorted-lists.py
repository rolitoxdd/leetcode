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
                    current_res.next = current0
                    current0 = current0.next
                else:
                    current_res.next = current1
                    current1 = current1.next
                current_res = current_res.next
            current_res.next = current0 or current1
            return dummy_head.next
                
        else:
            return self.mergeKLists(
                [
                    self.mergeKLists(lists[:len(lists)//2]), 
                    self.mergeKLists(lists[len(lists)//2:])
                ]
            )

#class Solution:
#    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#        if not lists:
#            return None
#        if len(lists) == 1:
#            return lists[0]
#        
#        mid = len(lists) // 2
#        left = self.mergeKLists(lists[:mid])
#        right = self.mergeKLists(lists[mid:])
#        
#        return self.merge(left, right)
#    
#    def merge(self, l1, l2):
#        dummy = ListNode(0)
#        curr = dummy
#        
#        while l1 and l2:
#            if l1.val < l2.val:
#                curr.next = l1
#                l1 = l1.next
#            else:
#                curr.next = l2
#                l2 = l2.next
#            curr = curr.next
#        
#        curr.next = l1 or l2
#        
#        return dummy.next

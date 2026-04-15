# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        return self.mergeRange(lists, 0, len(lists) - 1)

    def mergeRange(self, lists, left, right):
        if left == right:
            return lists[left]

        mid = (left + right) // 2
        leftList = self.mergeRange(lists, left, mid)
        rightList = self.mergeRange(lists, mid + 1, right)

        return self.mergeTwoLists(leftList, rightList)

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        curr.next = l1 if l1 else l2
        return dummy.next
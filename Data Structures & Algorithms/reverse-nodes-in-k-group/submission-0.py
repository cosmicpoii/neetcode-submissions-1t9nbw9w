# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 4 steps:
        # 1. find the kth point, if meet null for k steps from cur that break
        # 2. save the kth.next node to link
        # 3. reverse the k numbers of nodes
        # 4. relink

        dummy = ListNode(0, head)
        prev_tail = dummy

        while True:
            kth = self.getKth(prev_tail, k)
            if not kth:
                break

            # this group's first node
            curr = prev_tail.next
            # save next group's starting point
            nxt = kth.next

            # reverse
            self.reverse(curr, kth)

            # relink
            prev_tail.next = kth # the last group's tail -> this group's head
            curr.next = nxt

            prev_tail = curr # ??? move prev_tail this tail to prepare for the next group???

        return dummy.next
            
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

    def reverse(self, head, tail):
        prev = tail.next
        curr = head

        while prev != tail:
            nxt = curr.next # save the next node to avoid lose it
            curr.next = prev # reverse the direction
            prev = curr
            curr = nxt

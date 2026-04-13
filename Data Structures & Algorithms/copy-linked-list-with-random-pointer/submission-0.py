"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        map = {}

        cur = head
        while cur:
            map[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            copy = map[cur]
            copy.next = map.get(cur.next)
            copy.random = map.get(cur.random)
            cur = cur.next

        return map[head]
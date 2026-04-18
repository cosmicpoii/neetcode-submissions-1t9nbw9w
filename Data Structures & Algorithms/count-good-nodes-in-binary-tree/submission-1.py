# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
        good: if the node >= the biggest value from the path from the root to the node
        Four steps:
        step 1: start from root, make the biggest node value == root
        step 2: when arrive at one node, compare this node.val with biggest value
                - if node.val > biggest, then update biggest == node.val, count + 1
                - else: keep biggest and count number
        step 3: deliver the biggest to left and right subtree
        step 4: iterate until null, return 0
        '''
        count = 0

        if not root:
            return

        queue = deque([(root, root.val)])
        while queue:
            node, biggest = queue.popleft()
            if node.val >= biggest:
                biggest = node.val
                count += 1

            if node.left:
                queue.append((node.left, biggest))
            if node.right:
                queue.append((node.right, biggest))

        return count
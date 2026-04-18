# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # add nodes to deque
        # pop the most right node (the first node)
        # add the right tree to deque, the add the left tree
        result = []

        if not root:
            return []

        queue = deque([root])

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()

                if i == 0:
                    result.append(node.val)

                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        return result
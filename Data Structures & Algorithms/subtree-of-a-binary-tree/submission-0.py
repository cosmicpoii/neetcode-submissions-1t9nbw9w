# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # 1. find the subRoot's head in root
        # case_1: not match then return False
        # case_2:
        # 2. use deque to iterate each val in subRoot whether equal to root's val
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.val == subRoot.val and self.isSameTree(node, subRoot):
                return True

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return False

    def isSameTree(self, n, s):
        if not n and not s:
            return True
        if not n or not s:
            return False
        return n.val == s.val and self.isSameTree(n.left, s.left) and self.isSameTree(n.right, s.right)
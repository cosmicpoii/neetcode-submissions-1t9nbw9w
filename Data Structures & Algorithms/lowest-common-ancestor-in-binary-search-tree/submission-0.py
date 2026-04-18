# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # because BST: left tree < root < right tree, so there are three cases:
        # 1. p < node < q or one of q & p is the node: LCA is the node
        # 2. p, q < node: LCA in the left tree
        # 3. p, q > node: LCA in the right tree
        node = root

        while node:
            if p.val < node.val and q.val < node.val:
                node = node.left
            elif p.val > node.val and q.val > node.val:
                node = node.right
            else:
                return node

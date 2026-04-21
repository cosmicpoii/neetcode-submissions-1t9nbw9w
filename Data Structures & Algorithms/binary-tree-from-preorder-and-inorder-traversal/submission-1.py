# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # the first node in preorder is the root
        # beside the left of the first node in inorder is the left_tree
        # beside the right of the first node in inorder is the right_tree
        # do the same thing in left and right tree

        if not preorder:
            return None

        root_val = preorder[0]
        root = TreeNode(root_val)

        mid = inorder.index(root_val)

        root.left = self.buildTree(preorder[1 : 1 + mid], inorder[: mid])
        root.right = self.buildTree(preorder[1 + mid : ], inorder[mid+1:])

        return root
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # add the most right node to the list in each level
        # if there is no node in right side, then find the left side

        result = []

        def dfs(node, level):
            # base case: no node
            if not node:
                return

            if len(result) == level:
                result.append(node.val)

            dfs(node.right, level + 1)
            dfs(node.left, level + 1)

        # at the root
        dfs(root, 0)
        return result
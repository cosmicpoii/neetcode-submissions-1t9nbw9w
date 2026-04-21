# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''
        for any one node, there are only two cases:
            1. as the center node connect the left and right:
                   1
                 2   3 --> path: 2 -> 1 -> 3
            2. as the transfer that give the value to parent
        '''
        global_max = float('-inf')
        
        def dfs(node):
            nonlocal global_max
            if not node:
                return 0
            
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            global_max = max(global_max, node.val + left + right)

            return node.val + max(left, right)

        dfs(root)
        return global_max
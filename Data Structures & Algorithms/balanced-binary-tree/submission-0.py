# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(curr):
            if not curr: 
                return [True, 0]
            right = dfs(curr.right)
            left = dfs(curr.left)
            balanced = abs(right[1] - left[1])
            if balanced <= 1 and right[0] and left[0]: 
                return[True, 1 + max(right[1], left[1])]
            else : 
                return [False, 1 + max(right[1], left[1])]
        return dfs(root)[0]
                
        



        
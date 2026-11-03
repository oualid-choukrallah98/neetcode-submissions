# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0
        level = 0 
        q = deque([root])
        while q: 
            for i in range(len(q)):
                curr = q[0] 
                if curr.right:
                    q.append(curr.right) 
                if curr.left: 
                    q.append(curr.left)

                q.popleft()
            level += 1
        return level 

                



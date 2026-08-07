# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    @lru_cache
    def maxDepth(self, root: Optional[TreeNode], h: int = 0) -> int:
        print("ENTER :)")
        if not root:
            return h
        return max(self.maxDepth(root.left, h + 1), self.maxDepth(root.right, h + 1))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def helper(root):
    if not root:
        return []
    if not root.left and not root.right:
        return [root.val]

    return helper(root.left) + helper(root.right)

class Solution:
    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        

        return helper(root1) == helper(root2)
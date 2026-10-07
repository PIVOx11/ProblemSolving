# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def dfs(node, prev):
    if not node:
        return 0
    ans = 0
    if node.val >= prev:
        prev = node.val
        ans = 1

    ans += dfs(node.left, prev)
    ans += dfs(node.right, prev)
    return ans

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return dfs(root, root.val)


            
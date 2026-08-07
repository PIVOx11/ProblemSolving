# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


@lru_cache
def seq(root: Optional[TreeNode], arr: Optional([tuple])) -> [tuple]:
    if not arr:
        arr = ()

    if not root:
        return arr

    if not root.left and not root.right:
        arr = (*arr, root.val)
        return arr

    return seq(root.left, arr) + seq(root.right, arr)


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return seq(root1, None) == seq(root2, None)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        left_bound, right_bound = p.val, q.val
        cur = root
        while cur:
            if left_bound < cur.val and right_bound < cur.val:
                cur = cur.left
            elif left_bound > cur.val and right_bound > cur.val:
                cur = cur.right
            else:
                return cur
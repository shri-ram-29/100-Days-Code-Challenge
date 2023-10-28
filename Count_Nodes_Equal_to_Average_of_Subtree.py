# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            nonlocal count
            if not node:
                return 0, 0
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)
            subtree_sum = node.val + left_sum + right_sum
            subtree_count = 1 + left_count + right_count
            average = subtree_sum // subtree_count
            if node.val == average:
                count += 1
            return subtree_sum, subtree_count

        count = 0
        dfs(root)
        return count
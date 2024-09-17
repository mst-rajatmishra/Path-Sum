from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Base case: if the tree is empty
        if not root:
            return False
        
        # If we reach a leaf node
        if not root.left and not root.right:
            return root.val == targetSum
        
        # Recur for left and right subtrees with the updated targetSum
        newTargetSum = targetSum - root.val
        return (self.hasPathSum(root.left, newTargetSum) or
                self.hasPathSum(root.right, newTargetSum))

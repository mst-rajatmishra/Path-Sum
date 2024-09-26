from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, currentSum):
            # Base case: if the tree is empty
            if not node:
                return False
            
            currentSum += node.val  # Update the current sum
            
            # If we reach a leaf node
            if not node.left and not node.right:
                return currentSum == targetSum  # Compare to the original targetSum
            
            # Recur for left and right subtrees with the updated current sum
            return dfs(node.left, currentSum) or dfs(node.right, currentSum)
        
        return dfs(root, 0)

# Example Usage
# Constructing a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

s = Solution()
ans = s.hasPathSum(root, 5)
print(ans)  # Output: True

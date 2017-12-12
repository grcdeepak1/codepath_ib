# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isBalanced(self, root):
        return self.isBalancedInt(root)>=0

    def isBalancedInt(self, root):
        if root == None:
            return 0;
        left = self.isBalancedInt(root.left)
        right = self.isBalancedInt(root.right)
        if left<0 or right<0 or abs(left-right)>1:
            return -1
        return max(left,right)+1
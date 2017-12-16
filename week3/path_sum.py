# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def hasPathSum(self,node, s):

        # Return true if we run out of tree and s = 0
        if node is None:
            return (s == 0)

        else:
            ans = 0

            # Otherwise check both subtrees
            subSum = s - node.val
            # If we reach a leaf node and sum becomes 0, then
            # return True
            if(subSum == 0 and node.left == None and node.right == None):
                return True

            ans = ans or self.hasPathSum(node.left, subSum)
            ans = ans or self.hasPathSum(node.right, subSum)

            return ans


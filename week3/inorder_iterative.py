# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorderTraversal(self, A):
        current = A
        stack = []
        done = False
        result = []
        while (not done):
            if (current != None):
                stack.append(current)
                current = current.left
            else:
                if (len(stack) > 0):
                    current = stack.pop()
                    result.append(current.val)
                    current = current.right
                else:
                    done = True
        return result
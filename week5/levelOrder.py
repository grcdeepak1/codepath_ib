# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers

    def levelOrder(self, root):
        def height(node):
            if node == None:
                return 0
            lheight = height(node.left)
            rheight = height(node.right)

            if lheight > rheight:
                return lheight+1
            else:
                return rheight+1

        def printGivenLevel(root , level, ans):
            if root is None:
                return
            if level == 1:
                ans.append(root.val)
            elif level > 1:
                printGivenLevel(root.left , level-1, ans)
                printGivenLevel(root.right , level-1, ans)

        h = height(root)
        ret = []
        for i in range(1, h+1):
            ans = []
            printGivenLevel(root, i, ans)
            ret.append(ans)
        return ret
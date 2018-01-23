class Solution:
    # @param A : head node of linked list
    # @return the root node in the tree

    def createTree(self, root, r):
        low=0
        high=len(r)-1
        if low<=high:
            mid=(low+high)/2
            root=TreeNode(r[mid])
            root.left=self.createTree(root.left,r[:mid])
            root.right=self.createTree(root.right,r[mid+1:])
            return root
        else:
            return root

    def sortedListToBST(self, A):
        r=[]
        while A!=None:
            r.append(A.val)
            A=A.next

        root=None
        return self.createTree(root,r)
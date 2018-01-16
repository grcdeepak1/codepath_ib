import sys
class Solution:
    # @param A : list of integers
    # @return an integer
    def findMinXor(self, A):
        A = sorted(A)
        minXor = sys.maxint
        for (a, b) in zip(A, A[1:]):
            xor =  a ^ b
            if xor < minXor:
                minXor = xor
        return minXor
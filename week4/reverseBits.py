class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        INT_LEN = 32
        ans = 0
        for i in range(0, INT_LEN):
            if A & (1<<i):
                ans |= (1 << (INT_LEN-1)-i)
        return ans

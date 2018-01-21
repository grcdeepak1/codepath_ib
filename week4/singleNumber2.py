class Solution:
    # @param A : tuple of integers
    # @return an integer

    def singleNumber(self, A):
        INT_SIZE = 32
        ans = 0
        for i in range(0, INT_SIZE):
            sm = 0
            mask = 1 << i
            for j in A:
                if (j & mask):
                    sm += 1
            if (sm%3):
                ans |= mask
        return ans


s = Solution()
print(s.singleNumber([3, 2, 2, 4, 3, 3, 2]))
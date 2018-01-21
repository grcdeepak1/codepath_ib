
class Solution:
    # @param A : integer
    # @return a list of integers
    def grayCode(self, A):
        ans = []
        def grayCodeHelper(digits):
            if digits == 1:
                return ['0', '1']
            else:
                l1 = grayCodeHelper(digits-1)
                l2 = l1[::-1]
                for i in range(0, len(l1)):
                    l1[i] = str(l1[i]) + '0'
                    l2[i] = str(l2[i]) + '1'
                return l1 + l2
        for n in grayCodeHelper(A):
            ans.append(int(n,2))

        return ans

s = Solution()
print(s.grayCode(3))
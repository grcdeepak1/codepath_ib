class Solution:
    # @param A : list of integers
    # @return an integer
    def jump(self, A):
        n = len(A)
        if n == 0 or n == 1:
            return 0

        max_cur = 0
        steps = 0
        i=0
        while i < n:
            max_cur = i + A[i]
            if A[i] == 0:
                return -1
            else:
                steps += 1

            if max_cur >= n-1:
                return steps

            tmp = 0
            for j in range(i+1, max_cur+1):
                if A[j]+j > tmp:
                    tmp = A[j]+j
                    i = j

        return steps
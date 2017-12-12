class Solution:
    # @param A : list of list of integers
    # @param num : integer
    # @return an integer
    def searchMatrix(self, A, num):
        iMax = len(A)-1
        jMax = len(A[0])-1
        i = 0
        j = jMax

        while (i <= iMax and j >= 0):
            if (A[i][j] == num):
                return 1

            if (A[i][j] > num):
                j -= 1
            else:
                i += 1
        return 0
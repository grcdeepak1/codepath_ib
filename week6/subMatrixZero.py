dp = dict()
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        rows = len(A)
        cols = len(A[0])
        if rows == 0 or cols == 0:
            return 0

        sum_matrix = [[0 for i in range(cols+1)] for j in range(rows + 1)]
        result = 0

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                sum_matrix[i][j] = A[i-1][j-1] + sum_matrix[i-1][j] + sum_matrix[i][j-1] - sum_matrix[i-1][j-1]

        for  i in range(rows):
            for j in range(i+1, rows + 1):
                counti = {}
                counti[0] = 1
                for k in range(1, cols + 1):
                    val = sum_matrix[j][k] - sum_matrix[i][k]
                    if val in counti:
                        result = result + counti[val]
                        counti[val] = counti[val] + 1
                    else:
                        counti[val] = 1

        return result;
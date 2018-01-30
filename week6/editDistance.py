class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def minDistance(self, A, B):
        dp = [[0 for _ in range(len(A)+1)] for _ in range(len(B)+1)]

        for j in range(len(A)+1):
            dp[0][j] = j

        for j in range(1 , len(B)+1):
            dp[j][0] = j

        for i in range(1 , len(B)+1):
            for j in range(1 , len(A)+1):
                if B[i-1] == A[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])
        return dp[-1][-1]
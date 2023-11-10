class Solution:
    def knapSack(self, W, wt, val, n):
        # Initialize a 2D array to store the results of subproblems.
        dp = [[0] * (W + 1) for _ in range(n + 1)]

        # Build the dp array in a bottom-up manner.
        for i in range(1, n + 1):
            for j in range(W + 1):
                if wt[i - 1] <= j:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - wt[i - 1]] + val[i - 1])
                else:
                    dp[i][j] = dp[i - 1][j]

        # The final result is stored in the bottom-right cell of the dp array.
        return dp[n][W]
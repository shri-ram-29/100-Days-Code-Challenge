class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # To make change for 0 cents, you need 0 coins.

        for coin in coins:
            for amounts in range(coin, amount + 1):
                dp[amounts] = min(dp[amounts], dp[amounts - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1

"""
LeetCode #322 - Coin Change
Approach: Optimized - Bottom-Up DP (Coins over Amounts)
"""

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        showoutput(coins, amount)

        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if c <= a:
                    dp[a] = min(dp[a], dp[a - c] + 1)
        return dp[amount] if dp[amount] <= amount else -1

def showoutput(coins, amount):
    print(f" Coins are {coins}, amont is {amount} Change amount is ", end="")


if __name__ == "__main__":
    print("===="*19 )
    print(" " * 22 ,"> Optimized Solution <")
    print("====" * 19)
    print()
    
    sol = Solution()

    print(sol.coinChange([1, 2, 5], 11))       # Expected: 3
    print()
    print(sol.coinChange([2], 3))              # Expected: -1
    print()
    print(sol.coinChange([1], 0))               # Expected: 0
    print()
    print(sol.coinChange([1, 3, 4], 6))         # Expected: 2
    print()
    print(sol.coinChange([2, 5, 10, 1], 27))    # Expected: 4
    print()


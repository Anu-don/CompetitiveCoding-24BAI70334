"""
LeetCode #322 - Coin Change
Approach: Brute Force (plain recursion)

Time Complexity:  O(c ^ amount)
Space Complexity: O(amount)  -- recursion depth
"""

from typing import List

INF = float("inf")


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        showoutput(coins, amount)

        def solve(t):
            if t == 0:
                return 0
            best = INF
            for c in coins:
                if c <= t:
                    best = min(best, solve(t - c) + 1)
            return best

        ans = solve(amount)
        return ans if ans < INF else -1

def showoutput(coins, amount):
    print(f" Coins are {coins}, amont is {amount} Change amount is ", end="")

if __name__ == "__main__":
    print("==="*19 )
    print(" " * 17 ,"> Brute Force <")
    print("===" * 19)
    print()

    sol = Solution()

    print(sol.coinChange([1, 2, 5], 11))    # Expected: 3
    print()
    print(sol.coinChange([2], 3))           # Expected: -1
    print()
    print(sol.coinChange([1], 0))           # Expected: 0
    print()
    print(sol.coinChange([1, 3, 4], 6))     # Expected: 2
    print()

    # NOTE: [2, 5, 10, 1], amount=27 is slow with plain recursion,
    # so it's left out of this brute-force run (use optimized_solution.py for it).

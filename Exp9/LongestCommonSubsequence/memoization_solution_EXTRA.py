
from functools import lru_cache


def longest_common_subsequence(text1, text2):
    m, n = len(text1), len(text2)

    showo(text1, text2)

    @lru_cache(maxsize=None)
    def solve(i, j):
        if i == m or j == n:
            return 0
        if text1[i] == text2[j]:
            return 1 + solve(i + 1, j + 1)
        return max(solve(i + 1, j), solve(i, j + 1))

    result = solve(0, 0)
    solve.cache_clear()
    return result

def showo(text1, text2):
    print(f" Texts are {text1} and {text2}", end = " longest Common Subsequence are")


if __name__ == "__main__":
    print("==="*19 )
    print(" " * 17 ,"> Memoization Solution <")
    print("===" * 19)

   # Test Case 1
    print(longest_common_subsequence("abcdezoro", "aceluffy"))  # Expected: 3
    print()

    # Test Case 2
    print(longest_common_subsequence("abcbatman", "abcpower"))  # Expected: 3
    print()

    # Test Case 3
    print(longest_common_subsequence("abcanudon", "deffunction"))  # Expected: 0
    print()

def longest_common_subsequence(text1, text2):
    m, n = len(text1), len(text2)
    prev = [0] * (n + 1)
    curr = [0] * (n + 1)

    showo(text1, text2)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                curr[j] = prev[j - 1] + 1
            else:
                curr[j] = max(prev[j], curr[j - 1])
        prev, curr = curr, prev

    return prev[n]

def showo(text1, text2):
    print(f" Texts are {text1} and {text2}", end = " longest Common Subsequence are")


if __name__ == "__main__":
    print("==="*19 )
    print(" " * 17 ,"> Space Optimized <")
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
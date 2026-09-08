def BackTracing(candidates, target):
    result = []

    def backtrack(start, path, rem):
        if rem == 0:
            result.append(path[:])
            return

        for i in range(start, len(candidates)):
            if candidates[i] <= rem:
                path.append(candidates[i])
                backtrack(i, path, rem - candidates[i])
                path.pop()

    backtrack(0, [], target)
    return result


if __name__ == "__main__":
    print("=" * 40)
    print("      COMBINATION SUM")
    print("     By Backtracking")
    print("=" * 40)

    candidates = list(map(int, input("Enter candidates: ").split()))
    target = int(input("Enter target: "))

    ans = BackTracing(candidates, target)

    print("\nPossible Combinations:")
    if ans:
        for i, comb in enumerate(ans, 1):
            print(f"{i}. {comb}")
    else:
        print("No valid combination found.")
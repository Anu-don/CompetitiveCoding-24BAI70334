def bruteForce(candidates, target):
    result = set()

    def solve(rem, path):
        if rem == 0:
            result.add(tuple(sorted(path)))
            return
        if rem < 0:
            return

        for num in candidates:
            solve(rem - num, path + [num])

    solve(target, [])
    return [list(x) for x in sorted(result)]


if __name__ == "__main__":
    print("=" * 40)
    print("      COMBINATION SUM")
    print("      By Brute Force")
    print("=" * 40)

    candidates = list(map(int, input("Enter candidates: ").split()))
    target = int(input("Enter target: "))

    ans = bruteForce(candidates, target)

    print("\nPossible Combinations:")
    if ans:
        for i, comb in enumerate(ans, 1):
            print(f"{i}. {comb}")
    else:
        print("No valid combination found.")
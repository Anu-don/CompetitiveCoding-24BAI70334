def backtrack(start, subset, nums):
    result.append(subset[:])

    for i in range(start, len(nums)):
        subset.append(nums[i])
        backtrack(i + 1, subset, nums)
        subset.pop()



if __name__ == "__main__":
    print("          Exp 2.1 SubSets")
    print("       Approach: Backtracking\n")

    n = int(input("Enter Number of length: "))

    nums = [int(input(f"Enter {i+1}: ")) for i in range(n)]
    nums = list(set(nums))


    result = []
    backtrack(0, [], nums)

    print(f"Subset is {result}")
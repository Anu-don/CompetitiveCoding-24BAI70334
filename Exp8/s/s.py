def stepfuntion(nums):
    l = len(nums)
    if l < 2:
        return l

    for i in range(l):

        n = 1
        for j in nums:
            if j < n:
                




    
if __name__ == "__main__":
    print("  "*5, "Exp 8 ")
    print(" "*5, "Solution")

    n = int(input("Enter lenght: "))
    l = [int(input(f"Enter {i+1}")) for i in range(n)]

    stepfunction(l)

    print("--"*5, "Done Completed", "--"*5)

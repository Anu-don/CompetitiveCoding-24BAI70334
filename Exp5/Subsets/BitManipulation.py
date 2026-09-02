def BitManipulation(num):
    l = len(num)
    if l < 2:
        return l + 1
    
    setn = []
    for i in range(1 << l):
        subset = []
        
        for j in range(l):
            if i & (1 << j):
                subset.append(num[j])
            
        setn.append(subset)
    
    print(f" Total length of SubSet is {len(setn)}.")
    return setn        
            
if __name__ == "__main__":
    print("         Exp 2.1 SubSets")
    print("       Approach Bit Manipulation\n")
    
    n = int(input("Enter Number of length "))
    num = set([int(input(f"Enter {i+1}: ")) for i in range(n)])
    
    num = list(num)
    num = BitManipulation(num)
    
    print(f"Subset is {num}")
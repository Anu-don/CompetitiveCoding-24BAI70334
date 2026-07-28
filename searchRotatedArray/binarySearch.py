def binarySearch(arr, tar):
    
    n = len(arr)
    
    lnum = arr[0]
    lindex = 0
    for i in range(n):
        if lnum > arr[i]:
            lnum = arr[i]
            lindex = i   
    
    print(lnum, lindex)
            
    if tar < arr[0]:
        start, end = i, n-1
    else:
        start, end = 0, i-1
       
    mid = (start + end)//2 
    while start < end:
        print(start, end, mid)
        
        if tar < arr[mid]:
            end = mid - 1
        elif tar > arr[mid]:
            start = mid
        elif tar == arr[mid]:
            print(f" Element present at Index {mid}") 
            return mid
        
        mid = (start + end)//2
                 
            
    return -1

if __name__ == "__main__":
    # print(" "*10," Binary Search\n")
    # n = int(input(" Enter length of array: "))
    
    # print()
    # arr = [int(input(f" Element {i} : ")) for i in range(n)]
    
    # tar = int(input(" Enter Target Value: "))
    # print()
    
    # print(f"     >>>  Output: {binarySearch(arr,tar)}")
    print("\n -----------------------------------------------------\n")
    print(f"     >>>  Output: {binarySearch([4,5,6,0,1,2,3],2)}")
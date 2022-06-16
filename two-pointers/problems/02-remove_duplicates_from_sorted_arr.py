def removeDuplicates(nums):
    l , r = 0 , 1
    length = 1
    
    while r < len(nums):
        if nums[l] != nums[r]:
            l += 1
            nums[l] = nums[r]
            length += 1
            
        r += 1
     
    return length
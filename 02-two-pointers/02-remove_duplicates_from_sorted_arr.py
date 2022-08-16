def removeDuplicates(nums):
    l , r = 0 , 1
    res_length = 1
    
    while r < len(nums):
        if nums[l] != nums[r]:
            l += 1
            nums[l] = nums[r]
            res_length += 1

        r += 1
     
    return res_length

    
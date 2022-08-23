def missingNumber(nums):
    i = 0
    
    while i < len(nums):
        correct_pos = nums[i]
        
        if nums[i] != nums[correct_pos]:
            nums[i] , nums[correct_pos] = nums[correct_pos], nums[i]
        else: i += 1
            
    for n in range(len(nums)):
        if n != nums[n]: return n

    return len(nums) # eg [0,1] -> 2
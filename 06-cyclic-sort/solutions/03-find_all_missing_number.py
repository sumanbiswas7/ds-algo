def findDisappearedNumbers(nums):
    i = 0
    while i < len(nums):
        correct_pos = nums[i] - 1
        
        if nums[i] <= len(nums) and nums[i] != nums[correct_pos]:
            nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
        else: i += 1
        
    missingNumbers = []
    for n in range(len(nums)):
        if nums[n] != n+1: missingNumbers.append(n+1)
    
    return missingNumbers
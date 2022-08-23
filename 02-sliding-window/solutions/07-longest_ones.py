# Longest Subarray with Ones after Replacement 
# Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
# Output: 6

# Optimal
def longestOnes(nums, k):
    oneCount = 0
    res = 0
    start = 0
    for end in range(len(nums)):
        if nums[end] == 1: oneCount += 1
        
        while (end-start+1) - oneCount > k:
            if nums[start] == 1: oneCount -= 1
            start += 1
        
        res = max(res , (end-start+1))
        
    return res

# Naive
def longestOnes2(nums, k):
    char_count = {}
    win_start = 0
    max_len = 0
    one_present = False
    
    for win_end in range(len(nums)):
        char_count[nums[win_end]] = 1 + char_count.get(nums[win_end] , 0)
        if nums[win_end] == 1: one_present = True

        if one_present:
            while (win_end-win_start+1) - char_count[1] > k:
                char_count[nums[win_start]] -= 1
                win_start += 1
        
        max_len = max(max_len , win_end - win_start + 1)
    
    return max_len


longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3)


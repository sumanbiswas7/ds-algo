#  EASY
def findMaxConsecutiveOnes(nums):
    win_start = 0
    max_len = 0
    
    for win_end in range(len(nums)):
        
        if nums[win_end] == 0:
            while nums[win_start] != 1:
                print(win_start)
                win_start += 1
            
        max_len = max(win_end - win_start + 2, max_len)

    print(max_len)
    return max_len
            
findMaxConsecutiveOnes([1,1,0,1,1,1])

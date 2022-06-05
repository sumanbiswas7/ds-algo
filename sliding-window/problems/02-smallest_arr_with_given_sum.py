# Given an array of positive numbers and a positive number ‘S’, find the length of the smallest 
# contiguous subarray whose sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.

# Input: [2, 1, 5, 2, 3, 2], S=7 
# Output: 2
# Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].

import sys
def minSubArrayLen(nums, target):
    min_len = sys.maxsize
    win_start = 0
    win_sum = 0
    for win_end in range(len(nums)):
        win_sum += nums[win_end]

        print(win_start , win_end)

        while win_sum >= target:
            min_len = min(win_end-win_start + 1, min_len)
            win_sum -= nums[win_start]
            win_start += 1
            
    if min_len == sys.maxsize:
        return 0
    
    return min_len

minSubArrayLen([2, 5, 5, 2, 3, 2], 7)





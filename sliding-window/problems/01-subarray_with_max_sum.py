# Input: [2, 1, 5, 1, 3, 2], k=3 
# Output: 9
# Explanation: Subarray with maximum sum is [5, 1, 3].

import sys
def subArrWithMaxSum(nums,k):
    maxSum = -sys.maxsize
    tempSum = 0
    i = 0
    while i < k:
        tempSum += nums[i]        
        i += 1 
    maxSum = max(tempSum, maxSum)

    while i < len(nums):
        tempSum = (tempSum + nums[i]) - nums[i-k]
        maxSum = max(tempSum, maxSum)
        i += 1

    print(maxSum)


test1 = [2, 1, 5, 1, 3, 2] 
k = 3
test2 = [2, 3, 4, 1, 5]
k2 = 2

subArrWithMaxSum(test2, 2)
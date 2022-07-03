# Problem Statement #
# Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is
# as close to the target number as possible, return the sum of the triplet. If there are more than 
# one such triplet, return the sum of the triplet with the smallest sum.

# Example 1:
# Input: [-2, 0, 1, 2], target=2
# Output: 1
# Explanation: The triplet [-2, 1, 2] has the closest sum to the target.

def threeSumClosest(self, nums: List[int], target: int) -> int:
    smallest = 9999
    res = 0
    nums.sort()
    
    for i in range(len(nums)):
        l , r = i+1 , len(nums)-1
        
        while l < r:
            threeSum = nums[i] + nums[l] + nums[r]
            difference = abs(target-threeSum)
            
            if difference < smallest:
                smallest = difference
                res = threeSum
            
            if threeSum > target:
                r -= 1
            else:
                l += 1
                
    return res
    
    
    
threeSumClosest([-2, 0, 1, 2], 2) 
threeSumClosest([-3, -1, 1, 2], 1)
threeSumClosest([1, 0, 1, 1], 100)
threeSumClosest([-1, 2, 1, -4], 1)
# Ans should be 1, 0 ,3, 2
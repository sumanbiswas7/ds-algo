# Pair with Target Sum (easy)
# Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

# Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

# Example 1:

# Input: [1, 2, 3, 4, 6], target=6
# Output: [1, 3]
# Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6

def twoSum(self, numbers, target):
    l , r = 0 , len(numbers)-1
    
    while l <= r:
        numSum = numbers[l] + numbers[r]
        if numSum < target:
            l += 1
        elif numSum > target:
            r -= 1
        else:
            return [l+1,r+1]
        
    return 0
            
            
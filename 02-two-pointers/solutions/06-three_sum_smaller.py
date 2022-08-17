# Count triplets with sum smaller than X 
# Given an array arr[] of distinct integers of size N and a value sum, the task is to find the count of triplets (i, j, k),
# having (i<j<k) with the sum of (arr[i] + arr[j] + arr[k]) smaller than the given value sum.

def triplateWithSmallerSum(nums,target):
    nums.sort()
    res = 0
    for i in range(len(nums)-2):
        l , r = i + 1 , len(nums) - 1
        while l < r:
            threeSum = nums[i] + nums[l] + nums[r]
            if threeSum >= target: r -= 1
            else:
                print(nums[i],nums[l],nums[r])
                # Else for current i and j, there can (k-j) possible third elements
                # that satisfy the constraint.
                res += r-l
                l += 1
    print(res)

# triplateWithSmallerSum([-1,0,2,3], 3)
triplateWithSmallerSum([-2 ,0 ,1 ,3], 5)

# -2,0,1,2,3
# i = 1 = 0
# j = 3 = 3
# target = 5



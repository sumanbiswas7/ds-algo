# DUTCH NATIONAL FLAG PROBLEM
# [2,1,0,0,1,2] sort -> [0,0,1,1,2,2]

def sortColors(nums):
    low , high = 0 , len(nums)-1
    mid = 0

    while mid <= high:
        if nums[mid] == 0:
            nums[mid] = nums[low]
            nums[low] = 0
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid] = nums[high]
            nums[high] = 2
            high -= 1

    print(nums)


sortColors([2,1,0,0,1,2])
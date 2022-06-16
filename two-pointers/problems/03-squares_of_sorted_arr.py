# Problem Statement #
# Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.

# Example 1:

# Input: [-2, -1, 0, 2, 3]
# Output: [0, 1, 4, 4, 9]
# Example 2:

# Input: [-3, -1, 0, 1, 2]
# Output: [0 1 1 4 9]

def squareArr3(nums):
    squares = []

    for i in nums:
        squareNum = i * i
        squares.append(squareNum)

    squares.sort()
    print(squares)

def squareArr2(nums):
    for i in range(len(nums)):
        char = nums[i]
        nums[i] = char * char
    
    nums.sort()

    print(nums)

def squareArr(nums):
    # OPTIMAL
    l , r = 0 , len(nums) - 1
    squares = []

    while l <= r:
        leftSquare = nums[l] * nums[l]
        rightSquare = nums[r] * nums[r]

        if leftSquare > rightSquare:
            squares.append(leftSquare)
            l += 1
        else:
            squares.append(rightSquare)
            r -= 1

    squares.reverse()
    print(squares)



nums = [-2, -1, 0, 2, 3]
nums = [-3, -1, 0, 1, 2]
squareArr(nums)

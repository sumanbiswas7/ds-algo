# Algorithms Interview

understand coding problems pattern to build a good base on solving problems and preapre for interview :)

## Table of contents

| No  | Difficulty | Sliding Window                                       |
| --- | ---------- | ---------------------------------------------------- |
| 1   | Easy       | [Subarray with max sum](#subarray-with-max-sum)      |
| 2   | Medium     | [Smallest array with given sum](#sliding-win-2)      |
| 3   | Medium     | [longest substring with k character](#sliding-win-3) |
| 4   | Medium     | [Fruits into busket](#sliding-win-3)                 |

## Answers

### Subarray with max sum

[Problem Link](https://leetcode.com/problems/maximum-subarray/) <br/>
Solution : we'll initialize max-sum to given nums array's first element

```python
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
maxSum = nums[0]
```

we'll also gonna keep track of the total sum so far in a totalSum variable. loop through the nums array and keep updating totalSum. And whenever we get a negative value in totalSum we’ll update it to 0. That' it.

```python
def maxSubArray(nums):
    maxSum = nums[0]
    totalSum = 0

    for i in range(len(nums)):
        if totalSum < 0: totalSum = 0
        totalSum += nums[i]
        maxSum = max(totalSum , maxSum)

    return maxSum
```

<br/>**[⬆ Back to Top](#table-of-contents)**

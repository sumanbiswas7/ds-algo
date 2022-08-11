# Algorithms Interview

understand coding problem patterns to build a good base on solving problems. all answers are in python but if you get the idea you can implement these in any language and clinch your tech interview :)

## Table of contents

| No  | Difficulty | Sliding Window                                                     |
| --- | ---------- | ------------------------------------------------------------------ |
| 01  | Medium     | [Maximum Sum Subarray of Size K ](#maximum-sum-subarray-of-size-k) |
| 02  | Medium     | [Smallest array with given sum](#smallest-array-with-given-sum)    |
| 03  | Medium     | [longest substring with k character](#sliding-win-3)               |
| 04  | Medium     | [Fruits into busket](#sliding-win-3)                               |

## Answers

### Maximum Sum Subarray of Size K

[Problem Link](https://leetcode.com/problems/maximum-subarray/) <br/>
Question : Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.<br/>
Solution : Store the sum of the first k elements. This will be our starting window

```python
totalSum = 0
i = 0
    while i < k:
        totalSum += nums[i]
        i += 1
```

Then we can increment the window by one and in each incrementation, we’ll add the new element to totalSum and subtract the starting element (to keep the window k size).

```python
import sys
def subArrWithMaxSum(nums,k):
    maxSum = -sys.maxsize
    totalSum = 0
    i = 0
    while i < k:
        totalSum += nums[i]
        i += 1
    maxSum = max(totalSum, maxSum)

    while i < len(nums):
        totalSum = (totalSum + nums[i]) - nums[i-k]
        maxSum = max(totalSum, maxSum)
        i += 1

    return maxSum;
```

<br/>**[⬆ Back to Top](#table-of-contents)**

### Smallest array with given sum

[Problem Link](https://leetcode.com/problems/minimum-size-subarray-sum/) <br/>
Question : From array of nums and a positive number target, find the length of the smallest contiguous subarray whose sum is greater than or equal to target.<br/>
Solution : First, we'll find a window in which the sum is >= target. Then we’ll start shrinking the window (win_start -= 1) and whenever we get a window_sum < target, we’ll get out of the while loop and increment window_end.

```python
def minSubArrayLen(target: int, nums: List[int]):
    min_len = sys.maxsize
    window_sum = 0
    win_start = 0

    for win_end in range(len(nums)):
        window_sum += nums[win_end]

        while window_sum >= target:
            min_len = min( win_end-win_start + 1, min_len ) # We'll only update the min_len if win_sum is >= target
            window_sum -= nums[win_start]
            win_start += 1


    if (min_len == sys.maxsize): return 0
    return min_len
```

<br/>**[⬆ Back to Top](#table-of-contents)**

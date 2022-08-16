# Two Pointers

In problems where we deal with sorted arrays (or LinkedList) and need to find a set of elements that fulfill certain constraints, the Two Pointers approach becomes quite useful. Usually, we’ll start with one pointer at the start and one at the end or maybe two at the start or end, and depending on the condition we’ll operate the pointers.

## Table of contents

| No  | Difficulty | `Two Pointers`                                                              |
| --- | ---------- | --------------------------------------------------------------------------- |
| 01  | Easy       | [Two sum ](#two-sum)                                                        |
| 02  | Easy       | [Remove duplicates from sorted array](#remove-duplicates-from-sorted-array) |
| 03  | Easy       | [Squaring a Sorted Array](#squaring-a-sorted-array)                         |
| 04  | Medium     | [Three sum](#three-sum)                                                     |
| 05  | Medium     | [Three sum closest](#three-sum-closest)                                     |
| 06  | Medium     | [Three sum smaller](#three-sum-smaller)                                     |
| 07  | Medium     | [Dutch national flag problem](#dutch-national-flag)                         |

## Answers

### Two sum

[Problem Link](https://leetcode.com/problems/two-sum/) <br/>
Question : Probably you’ve solved thr infamous Two sum problem it already except here the given array is sorted.<br/>
Solution : Since the array is sorted we could use a more optimal approach. we'll create two pointers one at the start of the array and one at the end of the array and we’ll take the sum of them `arr[left] + arr[right]` if the sum is > required sum we’ll decrement the right pointer if it’s < required sum we’ll increment the left pointer or if we get the required sum we’ll return

```python
def twoSum(self, numbers, target):
    l , r = 0 , len(numbers)-1

    while l < r:
        numSum = numbers[l] + numbers[r]
        if numSum < target:
            l += 1
        elif numSum > target:
            r -= 1
        else:
            return [l+1,r+1]

    return 0
```

<br/>**[⬆ Back to Top](#table-of-contents)**

### Remove duplicates from sorted array

[Problem Link](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) <br/>
Question : Given an array of sorted numbers, remove all duplicates from it. <br/>
Solution : We’ll have to return the length of the return non-duplicate array after replacing the given array.

```python
Given -> [0,0,1,1,1,2,2,3,3,4]
Output -> 5
    and the given array should be like below
    [0,1,2,3,4,_,_,_,_,_] # “_” could be anything doesn’t matter
```

We’ll start our pointer from `i = 0` and `j = 1`. We’ll check if values at ith and jth are equal or not if they are equal we’ll simply increment the j by 1 and if they are unequal we’ll do

```python
i += 1 # otherwise ith element will be lost
nums[i] = nums[r] # placing the non-duplicates to the front
res_len += 1
```

Full Solution :

```python
def removeDuplicates(nums):
    l , r = 0 , 1
    res_length = 1

    while r < len(nums):
        if nums[l] != nums[r]:
            l += 1
            nums[l] = nums[r]
            res_length += 1

        r += 1

    return res_length
```

<br/>**[⬆ Back to Top](#table-of-contents)**

### Squaring a Sorted Array

[Problem Link](https://leetcode.com/problems/squares-of-a-sorted-array/) <br/>
Question : Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.<br/>
Solution : Will be updated

<br/>**[⬆ Back to Top](#table-of-contents)**

### Three sum

[Problem Link](https://leetcode.com/problems/3sum/) <br/>
Question : Given an integer array nums, return all the triplets that sums to zero.<br/>
Solution : Will be updated

<br/>**[⬆ Back to Top](#table-of-contents)**

### Three sum closest

[Problem Link](https://leetcode.com/problems/3sum-closest/) <br/>
Question : Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.<br/>
Solution : Will be updated

<br/>**[⬆ Back to Top](#table-of-contents)**

### Three sum smaller

[Problem Link](https://leetcode.com/problems/3sum-smaller/) <br/>
Question : Given an array arr of unsorted numbers and a target sum, count all triplets in it such that arr[i] + arr[j] + arr[k] < target.<br/>
Solution : Will be updated

<br/>**[⬆ Back to Top](#table-of-contents)**

### Dutch national flag

[Problem Link](https://leetcode.com/problems/sort-colors/) <br/>
Question : Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.<br/>
Solution : Will be updated

<br/>**[⬆ Back to Top](#table-of-contents)**

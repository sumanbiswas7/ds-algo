# Cyclic sort

This pattern describes an interesting approach to deal with problems involving arrays containing numbers in a given range. For example, take the following problem:

You are given an unsorted array containing numbers taken from the range 1 to ‘n’. The array can have duplicates, which means that some numbers will be missing. Find all the missing numbers.

To efficiently solve this problem, we can use the fact that the input array contains numbers in the range of 1 to ‘n’. For example, to efficiently sort the array, we can try placing each number in its correct place, i.e., placing ‘1’ at index ‘0’, placing ‘2’ at index ‘1’, and so on. Once we are done with the sorting, we can iterate the array to find all indices that are missing the correct numbers. These will be our required numbers.

## Table of contents

| No  | Difficulty | `Cyclic sort`                                           |
| --- | ---------- | ------------------------------------------------------- |
| 01  | Easy       | [Cyclic sort](#cyclic-sort-problem)                     |
| 02  | Easy       | [Find the missing number](#find-the-missing-number)     |
| 03  | Easy       | [Find all missing number](#find-all-missing-number)     |
| 04  | Easy       | [Find the duplicate number](#find-the-duplicate-number) |
| 05  | Easy       | [Find all duplicate number](#find-all-duplicate-number) |

## Answers

### Cyclic sort problem

[Problem Link]() <br/>
Question : Sort the given array using cyclic sort<br/>
Solution : We’ll traverse through the array and if the current number `nums[i]` is not on the correct index we’ll swap the number with the number present in the correct idx. But before incrementing `i` we’ll make sure `nums[i]` is in the correct idx.

```python
def cyclicSort(nums):
    i = 0

    while i < len(nums):
        correct_idx = nums[i] - 1

        if (nums[i] != nums[correct_idx]):
            nums[i] , nums[correct_idx] = nums[correct_idx], nums[i]
        else:
            i += 1

    return nums
```

<br/>**[⬆ Back to Top](#table-of-contents)**

### Find the missing number

[Problem Link](https://leetcode.com/problems/missing-number/) <br/>
Question : Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.<br/>
Solution : Since the given array has distinct numbers in the range [0, n], we can use cyclic sort. By using cyclic sort every element will be placed in its correct position except one. We can loop through the array to check every number is on its correct position `nums[i] == i` if not we’ll return the position `i`.

```python
def missingNumber(nums):
    i = 0

    while i < len(nums):
        correct_pos = nums[i]

        if nums[i] != nums[correct_pos]:
            nums[i] , nums[correct_pos] = nums[correct_pos], nums[i]
        else: i += 1

    for n in range(len(nums)):
        if n != nums[n]: return n

    return len(nums) # eg [0,1] -> 2
```

Another approach : We could use n\*(n+1) / 2 formula then subtract given array's sum

<br/>**[⬆ Back to Top](#table-of-contents)**

### Find all missing number

[Problem Link](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/) <br/>
Question : Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.<br/>
Solution : Like the previous problem, we’ll use cyclic sort to put the numbers in their correct positions. Then we’ll traverse the array and append the numbers not in the correct positions to the result.

```python
def findDisappearedNumbers(nums):
    i = 0
    while i < len(nums):
        correct_pos = nums[i] - 1

        if nums[i] <= len(nums) and nums[i] != nums[correct_pos]:
            nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
        else: i += 1

    missingNumbers = []
    for n in range(len(nums)):
        if nums[n] != n+1: missingNumbers.append(n+1)

    return missingNumbers
```

<br/>**[⬆ Back to Top](#table-of-contents)**

### Find the duplicate number

[Problem Link]() <br/>
Question : Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), guarantee that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.<br/>
Solution : Like the previous problem, we’ll use cyclic sort to put the numbers in their correct positions. After that the duplicate number will be placed at the last index.

```python
def findDuplicate(nums):
    i = 0
    while i < len(nums):
        correct_pos = nums[i] - 1
        if nums[i] != nums[correct_pos]:
            nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
        else: i += 1

    return nums[-1]
```

<br/>**[⬆ Back to Top](#table-of-contents)**

### Find all duplicate number

[Problem Link](https://leetcode.com/problems/find-all-duplicates-in-an-array/) <br/>
Question : Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.<br/>
Solution : Following the cyclic sort approach, we will place each number at its correct index. After that, we will iterate through the array to find all numbers that are not at the correct indices. All these numbers are duplicates.

```python
def find_duplicates(nums):
    i = 0
    while i < len(nums):
        correct_pos = nums[i] - 1
        if nums[i] != nums[correct_pos]:
            nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
        else: i += 1

    duplicates = []
    for n in range(len(nums)):
        if (nums[n] != n+1): duplicates.append(nums[n])

    return duplicates
```

<br/>**[⬆ Back to Top](#table-of-contents)**

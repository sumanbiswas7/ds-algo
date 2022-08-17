# Two Pointers

In problems where we deal with sorted arrays (or LinkedList) and need to find a set of elements that fulfill certain constraints, the Two Pointers approach becomes quite useful. Usually, we’ll start with one pointer at the start and one at the end or maybe two at the start or end, and depending on the condition we’ll operate the pointers.

## Table of contents

| No  | Difficulty | `Two Pointers`                                                              |
| --- | ---------- | --------------------------------------------------------------------------- |
| 01  | Easy       | [Two sum sorted](#two-sum-sorted)                                           |
| 02  | Easy       | [Remove duplicates from sorted array](#remove-duplicates-from-sorted-array) |
| 03  | Medium     | [Squaring a Sorted Array](#squaring-a-sorted-array)                         |
| 04  | Medium     | [Three sum](#three-sum)                                                     |
| 05  | Medium     | [Three sum closest](#three-sum-closest)                                     |
| 06  | Medium     | [Three sum smaller](#three-sum-smaller)                                     |
| 07  | Medium     | [Dutch national flag problem](#dutch-national-flag)                         |

## Answers

### Two sum sorted

[Problem Link](https://leetcode.com/problems/two-sum/) <br/>
Question : Probably you’ve solved the infamous Two sum problem already, except here the given array is sorted.<br/>
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
Solution : We’ll initiate one pointer at the start `left = 0` and one at the end `right = len(nums)-1`. We’ll compare squares of the values present on those indexes and append the greater value in the result. After doing this operation while (left <= right) times we’ll get a non-increasing result array we’ll just have to reverse it. Note: if we do `while < right` rather that `left <= right` the middle value won’t be covered.

```python
def squareArr(nums):
    l , r = 0 , len(nums) - 1
    res = []

    while l <= r:
        leftSquare = nums[l] * nums[l]
        rightSquare = nums[r] * nums[r]

        if leftSquare > rightSquare:
            res.append(leftSquare)
            l += 1
        else:
            res.append(rightSquare)
            r -= 1

    res.reverse()
    print(squares)
```

<br/>**[⬆ Back to Top](#table-of-contents)**

### Three sum

[Problem Link](https://leetcode.com/problems/3sum/) <br/>
Question : Given an integer array nums, return all the triplets that sums to zero.<br/>
Solution : This problem is pretty much the same as the two-sum. First of all, we’ll sort the given array. Then by looping, we’ll fix our first element and for the second and third elements, we’ll use the two-pointer-sorted approach.

```python
def threeSum(nums):
    res = []
    nums.sort()

    for i in range(len(nums)):
        if i != 0 and nums[i] == nums[i-1]: continue # Note-1

        l , r = i + 1 , len(nums)-1
        while l < r:
            threeSum = nums[i] + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append([nums[i],nums[l],nums[r]])
                l += 1
                while nums[l] == nums[l-1] and l < r: l+= 1 # Note-2
    return res
```

`Note-1` : If ith value and the previous value are the same we'll get the same third element thus duplicate triplets will be generated. <br/>
`Note-2` : After doing l += 1 if lth value and the previous value are the same duplicate triplets will be generated.

<br/>**[⬆ Back to Top](#table-of-contents)**

### Three sum closest

[Problem Link](https://leetcode.com/problems/3sum-closest/) <br/>
Question : Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.<br/>
Solution : Similar to the three-sum problem we’ll sort the given array first. Then we’ll use the two-pointers approach, we’ll see if the current sum difference `currentThreeSum - targetSum` is lesser than the previous difference only then we’ll update the res and difference.

```python
def threeSumClosest(nums: List[int], target: int):
    nums.sort()
    res, diff = 0, sys.maxsize

    for i in range(len(nums)-2):
        l, r = i+1, len(nums)-1

        while l < r:
            threeSum = nums[i] + nums[l] + nums[r]
            currDiff = abs(target - threeSum)

            if currDiff < diff:
                res = nums[i]+nums[l]+nums[r]
                diff = currDiff

            if threeSum < target: l += 1
            else: r -= 1

    return res
```

<br/>**[⬆ Back to Top](#table-of-contents)**

### Three sum smaller

[Problem Link](https://leetcode.com/problems/3sum-smaller/) <br/>
Question : Given an array arr of unsorted numbers and a target sum, count all triplets in it such that arr[i] + arr[j] + arr[k] < target.<br/>
Solution : In this problem, the gotcha is incrementing the result_length.

```python
input_array = [-3, 2, 1, 7]
target = 6

after sorting -> [-3, 1, 2, 7]

let's say i = 0, l = 1, r = 3
threeSum = 5
we could'nt only add 1 in result since there are (r-l) number
of triplets with sum < target so we'll do
result += r-l
```

Full Solution :

```python
def three_sum_smaller(nums, target):
    res_len = 0
    nums.sort()
    for i in range(len(nums)-2):
        l , r = i+1, len(nums)-1

        while l < r:
            threeSum = nums[i] + nums[l] + nums[r]
            if threeSum >= target:
                r -= 1
            else:
                res_len += r-l
                l += 1

    return res_len
```

<br/>**[⬆ Back to Top](#table-of-contents)**

### Dutch national flag

[Problem Link](https://leetcode.com/problems/sort-colors/) <br/>
Question : Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.<br/>
Solution : We’ll use three-pointers low and mid at the start and high at the end. We’ll increment the mid-pointer till it collapses with the high pointer.<br/>
If `nums[mid]` is equals 0 we’ll swap it with low element and increment low and mid </br>
If `nums[mid]` is equals 1 we’ll just increment the mid-pointer <br/>
If `nums[mid]` is equals 2 we’ll swap it with high element and decrement high-pointer

```python
def sortColors(self, nums: List[int]) -> None:
    low, mid, high = 0, 0, len(nums)-1
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
    return nums
```

<br/>**[⬆ Back to Top](#table-of-contents)**

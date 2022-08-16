# Algorithms Interview

understand coding problem patterns to build a good base on solving problems. all answers are in python but if you get the idea you can implement these in any language and clinch your tech interview :)

## Table of contents

| No  | Difficulty | `Sliding Window`                                                                                          |
| --- | ---------- | --------------------------------------------------------------------------------------------------------- |
| 01  | Medium     | [Maximum Sum Subarray of Size K ](#maximum-sum-subarray-of-size-k)                                        |
| 02  | Medium     | [Smallest array with given sum](#smallest-array-with-given-sum)                                           |
| 03  | Medium     | [Longest substring with k character](#longest-substring-with-k-distinct-char)                             |
| 04  | Medium     | [Fruits into busket](#fruits-into-basket)                                                                 |
| 05  | Medium     | [Longest substr without repeating char](#longest-substr-without-repeating-char)                           |
| 06  | Hard       | [Longest substr with same letters after replacement](#longest-substr-with-same-letters-after-replacement) |
| 07  | Hard       | [Longest subarray with ones after replacement](#longest-subarray-with-ones-after-replacement)             |

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

### Longest substring with k distinct char

[Problem Link](https://www.lintcode.com/problem/386/) <br/>
Question : Given a string S, find the length of the longest substring T that contains at most k distinct characters.<br/>
Solution : We'll store every character’s occurrences in a hashtable.

```python
# char -> character got from loop
char_set = {}
char_set[char] = 1 + char_set.get(char , 0)
# if the char exists in hash .get will return it's count else it'll return 0

# char_set = { a:2, b:4, m:1 } example
```

now we want to keep an window which has no more than k char. if the window has more than k char we'll shrink it like below

```python
while len(char_set) > k:
# decrementing the counts until we get 0, then shrinking the window by del[char]
    char_set[start_char] -= 1
    if (char_set[start_char]) == 0: del char_set[start_char]
    win_start += 1
```

Full solution :

```python
def length_of_longest_substring_k_distinct(s: str, k: int):
  char_set = {}
  win_start, max_len = 0 , 0

  for win_end in range(len(s)):
    end_char = s[win_end]
    char_set[end_char] = 1 + char_set.get(end_char,0)

    while len(char_set) > k:
      start_char = s[win_start]
      char_set[start_char] -= 1
      if (char_set[start_char]) == 0: del char_set[start_char]
      win_start += 1

    max_len = max(win_end-win_start+1 , max_len)

  return max_len
```

<br/>**[⬆ Back to Top](#table-of-contents)**

### Fruits into basket

[Problem Link](https://leetcode.com/problems/fruit-into-baskets/) <br/>
Question : Given the integer array fruits, return the maximum number of fruits you can pick. (visit the problem) <br/>
Solution : We'll keep count of the fruits like [this](#longest-substring-with-k-distinct-char). We'll try to maintain a window that has no more than 2 type of fruits so the problem is identical to the problem [longest substring with k distinct char](#longest-substring-with-k-distinct-char) except k is 2 here.

```python
totalFruit(fruits: List[int]):
    fruit_set = {}
    win_start = 0
    res = -sys.maxsize

    for win_end in range(len(fruits)):
        end_fruit = fruits[win_end]
        fruit_set[end_fruit] = 1 + fruit_set.get(end_fruit,0)

    while len(fruit_set) > 2:
        start_fruit = fruits[win_start]
        fruit_set[start_fruit] -= 1
        if fruit_set[start_fruit] == 0: del fruit_set[start_fruit]
        win_start += 1

    res = max(res,win_end-win_start+1)

    if (res == -sys.maxsize): return 0
    return res
```

<br/>**[⬆ Back to Top](#table-of-contents)**

### Longest substr without repeating char

[Problem Link](https://leetcode.com/problems/longest-substring-without-repeating-characters/) <br/>
Question : Given a string s, find the length of the longest substring without repeating characters. <br/>
Solution : Similar to the previous problem we’ll use the sliding window method. We’ll create a hash_set and store the counts and whenever we get a char that is already present in the set we’ll shrink the window.`The only catch is we’ll have to check if the char already exists before adding it.` Go through the code and you’ll understand it.

```python
def lengthOfLongestSubstring(s):
    charSet = set()
    win_start = 0
    res = 0
    for win_end in range(len(s)):
        while s[win_end] in charSet:
            charSet.remove(s[win_start])
            win_start += 1

        charSet.add(s[win_end])

        res = max(win_end-win_start+1, res)

    return res
```

<br/>**[⬆ Back to Top](#table-of-contents)**

### Longest substr with same letters after replacement

[Problem Link](https://leetcode.com/problems/longest-repeating-character-replacement/) <br/>
Question : Given a string with uppercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement. <br/>
Solution : Consider a window “AABA” and given k = 1. If we subtract the max occurring char (“A”) from the window length we’ll get 1 (4-3). This 1 represents how many characters we’ll have to replace to get a window with the same characters.<br/> For window “ABAB” this value will be 2 (4-2). Our window will be valid only when this value is smaller or equals k.

```python
if  (window_length – max_occuring_char <= k): return window_valid
```

So whenever our window doesn’t meet this condition we’ll shrink the window.

```python
if (window_length – max(char.values()) > k): shrink
# max(char.values()) will return value of char with maximum count
```

```python
def characterReplacement(self, s, k):
    charCount = {}
    win_start = 0
    max_len = 0

    for win_end in range(len(s)):
        charCount[s[win_end]] = 1 + charCount.get(s[win_end],0)

        while ((win_end-win_start + 1) - max(charCount.values())) > k:
            charCount[s[win_start]] -= 1
            if (charCount[s[win_start]] == 0): del charCount[s[win_start]]
            win_start += 1

        max_len = max(max_len , win_end-win_start+1)

    return max_len
```

<br/>**[⬆ Back to Top](#table-of-contents)**

### Longest subarray with ones after replacement

[Problem Link](https://leetcode.com/problems/max-consecutive-ones-iii/) <br/>
Question : Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s. <br/>
Solution : This problem is identical to before except we have to take care of some edge cases and add a trigger before the while loop. <br/>
As given in the problem the longest consecutive number will be 1 so instead of calculating the max count of chars we’ll just count 1’s count `char_count[1]`. So our condition will be

```python
while (win_end-win_start+1) - char_count[1] > k: shrink window
```

Keep in mind since we are counting 1’s we only want to enter the while loop if we found at least one 1 so we’ll set a flag `one_present` if it’s true then we’ll enter the loop. And also if we come across a zero count of any number we don’t wanna delete it.

```python
if one_present:
    while (win_end-win_start+1) - char_count[1] > k:
        start_char = nums[win_start]
        char_count[start_char] -= 1
        win_start += 1
```

Full Solution

```python
def longestOnes(self, nums, k):
    char_count = {}
    win_start = 0
    max_len = 0
    one_present = False

    for win_end in range(len(nums)):
        char_count[nums[win_end]] = 1 + char_count.get(nums[win_end] , 0)
            if nums[win_end] == 1: one_present = True

            if one_present:
                while (win_end-win_start+1) - char_count[1] > k:
                    char_count[nums[win_start]] -= 1
                    win_start += 1

            max_len = max(max_len , win_end - win_start + 1)

    if not one_present and len(nums)>1: return 0
    return max_len
```

<br/>**[⬆ Back to Top](#table-of-contents)**

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

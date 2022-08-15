# Sliding Window


## Table of contents

| No  | Difficulty | Sliding Window                                                                                            |
| --- | ---------- | --------------------------------------------------------------------------------------------------------- |
| 01  | Medium     | [Maximum Sum Subarray of Size K ](#maximum-sum-subarray-of-size-k)                                        |
| 02  | Medium     | [Smallest array with given sum](#smallest-array-with-given-sum)                                           |
| 03  | Medium     | [Longest substring with k character](#longest-substring-with-k-distinct-char)                             |
| 04  | Medium     | [Fruits into busket](#fruits-into-basket)                                                                 |
| 05  | Medium     | [Longest substr without repeating char](#longest-substr-without-repeating-char)                           |
| 06  | Hard       | [Longest substr with same letters after replacement](#longest-substr-with-same-letters-after-replacement) |
| 07  | Hard       | [Longest subarray with ones after replacement](#longest-subarray-with-ones-after-replacement)             |

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

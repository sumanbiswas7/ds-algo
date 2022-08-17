# Hashing

## Table of contents

| No  | Difficulty | Sliding Window                                                |
| --- | ---------- | ------------------------------------------------------------- |
| 01  | Easy       | [Contains Duplicate](#contains-duplicate)                     |
| 02  | Easy       | [Two Sum](#two-sum)                                           |
| 03  | Easy       | [Valid Anagram](#valid-anagram)                               |
| 04  | Medium     | [Group Anagrams](#group-anagrams)                             |
| 05  | Medium     | [Top k frequent elements](#top-k-frequent-elements)           |
| 06  | Medium     | [Product of array expect self](#product-of-array-expect-self) |
| 07  | Medium     | [Valid soduku](#valid-soduku)                                 |
| 08  | Medium     | [Encode and decode strings](#encode-and-decode-strings)       |

## Answers

### Contains duplicate

[Problem Link](https://leetcode.com/problems/contains-duplicate/) <br/>
Question : Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.<br/>
Solution : Although we expect you to solve this one, but in case you’re a beginner please search for the solution on youtube :)

```python
def containsDuplicate(nums):
    hashset = set()
    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False

```

<br/>**[⬆ Back to Top](#table-of-contents)**

### Two sum

[Problem Link](https://leetcode.com/problems/two-sum/) <br/>
Question : Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
Solution : It’s a pity if you are not familiar with the two-sum problem. Please search for the problem on youtube right now!

```python
def twoSum(nums, target):
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
```

<br/>**[⬆ Back to Top](#table-of-contents)**

### Valid anagram

[Problem Link](https://leetcode.com/problems/valid-anagram/) <br/>
Question : Given two strings s and t, return true if t is an anagram of s, and false otherwise. An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.<br/>
Solution : First, we’ll store all elements from `s` with their occurrences in a hash-set. Then we’ll traverse through `t` and keep decrementing the count of the current element if it exists in the hash-set. At the end, if we get an empty hash-set we’ll return True.

```python
    def isAnagram(s, t):
        char_set = {}
        if len(s) != len(t): return False

        for e in s:
            char_set[e] = 1 + char_set.get(e,0)

        for e in t:
            if e in char_set:
                char_set[e] -= 1
                if char_set[e] == 0: del char_set[e]

        if len(char_set) > 0: return False
        else: return True
```

<br/>**[⬆ Back to Top](#table-of-contents)**

### Group anagrams

[Problem Link](https://leetcode.com/problems/group-anagrams/) <br/>
Question : Given an array of strings strs, group the anagrams together. You can return the answer in any order.
Solution : Coming soon...

<br/>**[⬆ Back to Top](#table-of-contents)**

### Top k frequent elements

[Problem Link]() <br/>
Question : Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
Solution : Coming soon...

<br/>**[⬆ Back to Top](#table-of-contents)**

### Product of array expect self

[Problem Link](https://leetcode.com/problems/product-of-array-except-self/) <br/>
Question : Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
Solution : Coming soon...

<br/>**[⬆ Back to Top](#table-of-contents)**

### Valid soduku

[Problem Link](https://leetcode.com/problems/valid-sudoku/) <br/>
Question : Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to soduku rules
Solution : Coming soon...

<br/>**[⬆ Back to Top](#table-of-contents)**

### Encode and Decode Strings

[Problem Link](https://www.lintcode.com/problem/659/) <br/>
Question : Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
Solution : Coming soon...

<br/>**[⬆ Back to Top](#table-of-contents)**

# Hashing

Assuming you’re familiar with the hashmap data structure. If you are then let’s learn some tricks.

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
Solution : For each and every word we can create a char-set [word -“big”, set - {‘b’: 1, ‘i’: 1, ‘g’:1} ] but rather we’ll create a tuple (0 ,0 ,0 …26) so that we can use this as a key and we’ll store the counts in it. Since one key can have more than one word our values will be array of words.

```python
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    char_set = {}
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
            if tuple(count) not in char_set: char_set[tuple(count)] = []
            char_set[tuple(count)].append(s)

    return char_set.values()
```

<br/>**[⬆ Back to Top](#table-of-contents)**

### Top k frequent elements

[Problem Link]() <br/>
Question : Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order. </br>
Solution : We’ll store number counts in char-set. Then we’ll use the counts as indices and numbers as values inside an array. For array `[2,1,1,4]` it’ll be `[ [], [2,4], [1], [] ]`. Then we’ll insert the values from end inside a res array until the length of res is not equals given k.

```python
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    char_set = {}
    freq = [[] for i in range(len(nums))]

    for n in nums: char_set[n] = 1 + char_set.get(n,0)
    for n, c in char_set.items(): freq[c].append(n)

    res = []
    for i in range(len(freq)-1,0,-1):
        for n in freq[i]:
        res.append(n)
        if len(res) == k: return res
```

<br/>**[⬆ Back to Top](#table-of-contents)**

### Product of array expect self

[Problem Link](https://leetcode.com/problems/product-of-array-except-self/) <br/>
Question : Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]. Note: You can't use the division operator :) <br/>
Solution : This solution requires visual and detailed representation please visit this [link](https://www.youtube.com/watch?v=bNvIQI2wAjk)

```python
def productExceptSelf(nums):
    output = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        output[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(len(nums)-1,-1,-1):
        output[i] *= postfix
        postfix *= nums[i]

    return output
```

<br/>**[⬆ Back to Top](#table-of-contents)**

### Valid soduku

[Problem Link](https://leetcode.com/problems/valid-sudoku/) <br/>
Question : Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to soduku rules
Solution : This solution requires visual and detailed representation please visit this [link](https://www.youtube.com/watch?v=TjFXEUCMqI8)

```python
def isValidSudoku(self, board):
    rows = collections.defaultdict(set)
    columns = collections.defaultdict(set)
    squares = collections.defaultdict(set)

    for r in range(9):
        for c in range(9):
            if board[r][c] == ".": continue

            if (board[r][c] in rows[r] or
                board[r][c] in columns[c] or
                board[r][c] in squares[(r//3,c//3)]): return False

                rows[r].add(board[r][c])
                columns[c].add(board[r][c])
                squares[(r//3 , c//3)].add(board[r][c])

    return True
```

<br/>**[⬆ Back to Top](#table-of-contents)**

# Subsets

A huge number of coding interview problems involve dealing with Permutations and Combinations of a given set of elements. This pattern describes an efficient Breadth First Search (BFS) approach to handle all these problems.

## Table of contents

| No  | Difficulty | `Subsets`                                           |
| --- | ---------- | --------------------------------------------------- |
| 01  | Medium     | [Subsets](#subsets)                                 |
| 02  | Medium     | [Subsets with duplicates](#subsets-with-duplicates) |

## Answers

### Subsets

[Problem Link](https://leetcode.com/problems/subsets/) <br/>
Question : Given a set with distinct elements, find all of its distinct subsets.<br/>
Solution 1: Let's say given input is `[1,5,3]` We can start with `res = [[]]` now we we'll add 1 in every array inside of res. now `res = [[],[1]]` we'll do similar process for the rest of elements in input array

<img src="assets/problem-01.png" width="450px"/> <br/>

```python
def subsets(nums):
    subsets = [[]]

    for n in nums:
        for i in range(len(subsets)):
            currSet = subsets[i].copy()
            currSet.append(n)
            subsets.append(currSet)

    return subsets
```

<br/>**[⬆ Back to Top](#table-of-contents)**

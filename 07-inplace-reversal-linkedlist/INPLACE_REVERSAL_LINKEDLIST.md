# Inplace reversal of a linkedlist

In a lot of problems, we are asked to reverse the links between a set of nodes of a LinkedList. Often, the constraint is that we need to do this in-place, i.e., using the existing node objects and without using extra memory. we will solve a bunch of problems using this pattern.

## Table of contents

| No  | Difficulty | `Inplace reversal of linkedlist`                                      |
| --- | ---------- | --------------------------------------------------------------------- |
| 01  | Easy       | [Reverse a linkedlist](#reverse-a-linkedlist)                         |
| 02  | Medium     | [Reverse a sublist](#reverse-a-sublist)                               |
| 03  | Medium     | [Reverse every K-element Sub-list](#reverse-every-k-element-sub-list) |

## Answers

### Reverse a linkedlist

[Problem Link](https://leetcode.com/problems/reverse-linked-list/) <br/>
Question : Given the head of a Singly LinkedList, reverse the LinkedList. Write a function to return the new head of the reversed LinkedList.<br/>
Solution : Given `1->2->3->null`, we’ll have to return `3->2->1->null`. We’ll create two variables previous and current and initialize them with None and head.

> 1.  Now we’ll replace the current node’s next to previous `current.next = previous`, and previous to current `previous = current`<br/> [ 1->null, previous = 1]. <br/>
> 2.  We’ll also have to store current’s next at first `nextnode = current.next` then replace the current node with nextnode to traverse the linkedlist

```python
def reverse(head):
    current = head, previous = None

    while current:
        nextnode = current.next
        current.next = previous
        previous = current
        current = nextnode

    return previous
```

<br/>**[⬆ Back to Top](#table-of-contents)**

### Reverse a sublist

[Problem Link]() <br/>
Question : Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the LinkedList from position ‘p’ to ‘q’. <br/>
Solution : Coming soon !

<br/>**[⬆ Back to Top](#table-of-contents)**

### Reverse every K-element Sub-list

[Problem Link]() <br/>
Question : Given the head of a LinkedList and a number ‘k’, reverse every ‘k’ sized sub-list starting from the head. If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too. <br/>
Solution : Coming soon !

<br/>**[⬆ Back to Top](#table-of-contents)**

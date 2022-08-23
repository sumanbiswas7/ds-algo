def reverse_between(head, left, right):
    dummy = ListNode(0, head)

    # 1) reach node at position left
    leftPrev, curr = dummy, head
    for i in range (left-1):
        curr, leftPrev = curr.next, curr
    prev = None

    # Now curr = left, prevLeft = node before left
    # 2) Reverse from left to right
    for i in range (right-left+1):
        tmpNext = curr.next
        curr.next, prev = prev, curr
        curr = tmpNext

    # 3) Update positions
    leftPrev.next.next = curr # curr is node after right
    leftPrev.next = prev # prev is right

    return dummy.next
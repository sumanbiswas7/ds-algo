def reverse(head):
    current = head, previous = None

    while current:
        nextnode = current.next
        current.next = previous
        previous = current
        current = nextnode

    return previous
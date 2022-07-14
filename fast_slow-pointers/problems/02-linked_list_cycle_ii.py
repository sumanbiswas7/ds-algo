def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    fast, slow, entry = head, head, head
    
    while fast and fast.next:
        slow, fast = slow.next , fast.next.next
        
        if slow == fast:
            while slow != entry:
                slow = slow.next
                entry = entry.next
            return entry
    
    return None
        
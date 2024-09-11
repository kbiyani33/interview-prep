def removeKthNode(head, k):
    temp, count = head, 0
    while temp:
        count += 1
        temp = temp.next
    
    if k==count:
        return head.next
    
    temp, passed = head, 0
    while temp:
        passed += 1
        if passed == count-k:
            deleted = temp.next
            if deleted: temp.next = deleted.next
            break
        temp = temp.next
    return head
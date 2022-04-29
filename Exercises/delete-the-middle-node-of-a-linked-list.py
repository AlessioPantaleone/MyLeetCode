class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


def deleteMiddle(head: ListNode) -> ListNode:
    beforemiddle = head
    headBK = head
    if head.next is None:
        return None
    if head.next is not None:
        head = head.next
        if head.next is not None:
            head = head.next
    while head.next is not None:
        beforemiddle = beforemiddle.next
        head = head.next
        if head.next is not None:
            head = head.next
    beforemiddle.next = beforemiddle.next.next
    return headBK

if __name__ == "__main__":
    L4 = ListNode(4)
    L3 = ListNode(3,L4)
    L2 = ListNode(2,L3)
    L1 = ListNode(1,L2)
    L0 = ListNode(0,L1)

    LL = deleteMiddle(L0)
    z = 1

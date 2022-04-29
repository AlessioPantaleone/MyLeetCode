class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


def isPalindrome(head: ListNode) -> bool:
    arr = []
    while head.next is not None:
        arr.append(head.val)
        head = head.next
    arr.append(head.val)
    if len(arr)%2 == 1:
        arr.pop(len(arr)//2)
    A = arr[:len(arr)//2]
    B = arr[len(arr)//2:]
    B.reverse()
    if A == B:
        return True
    else:
        return False

if __name__ == "__main__":
    L4 = ListNode(1)
    L3 = ListNode(2,L4)
    L2 = ListNode(2,L3)
    L1 = ListNode(1,L2)

    print(isPalindrome(L1))


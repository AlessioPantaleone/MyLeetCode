
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]):
        addends = [l1,l2]
        total = 0
        for list in addends:
            head = list
            power = 1
            while head is not None:
                total += head.val * power
                power *= 10
                head = head.next

        L= None
        for cifra in (str(total)):
            L = ListNode(int(cifra),L)
        return L




if __name__ == "__main__":
    S = Solution()

    L4 = ListNode(1)
    L3 = ListNode(0,L4)
    L2 = ListNode(0,L3)
    L1 = ListNode(0,L2)

    AAA = (S.addTwoNumbers(L1,L3))
    print("Finished")
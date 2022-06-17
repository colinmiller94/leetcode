# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, n1, n2):

        carry = 0

        current = results = ListNode()
        while n1 or n2 or carry:
            total = 0
            if n1:
                total += n1.val
                n1 = n1.next
            if n2:
                total += n2.val
                n2 = n2.next

            if carry:
                total += 1
            carry = 0
            if total > 9:
                total = total - 10
                carry = 1

            current.next = ListNode(total)
            current = current.next

        return results.next
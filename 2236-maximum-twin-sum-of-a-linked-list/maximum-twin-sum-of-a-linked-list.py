# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        slow = head
        fast = head

        # Find the middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half
        prev = None
        curr = slow

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Find maximum twin sum
        first = head
        second = prev
        ans = 0

        while second:
            ans = max(ans, first.val + second.val)
            first = first.next
            second = second.next

        return ans
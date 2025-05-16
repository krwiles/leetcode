# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def num_construct(self, node: ListNode) -> int:
        """Construct an integer from a linked list of digits."""
        place = 1
        num = 0

        while node:
            num += node.val * place
            place *= 10
            node = node.next

        return num

    def num_list_create(self, n: int) -> ListNode:
        """Construct a linked list from an integer."""
        head = node = ListNode(n % 10)
        n //= 10

        while n:
            node.next = ListNode(n % 10)
            node = node.next
            n //= 10

        return head

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # turn the two lists into integers and add them
        add = self.num_construct(l1) + self.num_construct(l2)

        # create and return a list from the result
        return self.num_list_create(add)

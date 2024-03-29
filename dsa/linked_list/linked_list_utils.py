from typing import Optional

from linked_list import ListNode
from singly_linked_list import SinglyLinkedList


def to_list(head: ListNode) -> list:
    ret = list()
    node = head
    while node:
        ret.append(node.data)
        node = node.next
    return ret


def to_singly_linked_list(elems: list) -> SinglyLinkedList:
    sll = SinglyLinkedList()
    for data in elems:
        sll.insert_at_tail(data)
    return sll


### Sum
def sum_linked_list_iterative(head: ListNode) -> int:  # Time: O(n), Space: O(1)
    sum = 0
    current = head
    while current:
        sum += int(current.data)
        current = current.next
    return sum


def sum_linked_list_recursive(head: ListNode) -> int:  # Time: O(n), Space: O(n)

    def recurse(current: ListNode):
        if current == None:
            return 0
        return current.data + recurse(current.next)

    return recurse(head)


### Reverse
def reverse_linked_list_iterative(head: ListNode) -> ListNode:
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


def reverse_linked_list_recursive(head: ListNode) -> ListNode:

    def recurse(current: ListNode, prev: ListNode = None) -> ListNode:
        if current == None:
            return prev
        next_node = current.next
        current.next = prev
        return recurse(next_node, current)

    return recurse(head)


### Merge sorted lists
def merge_sorted_lists_iterative(head1: ListNode, head2: ListNode) -> ListNode:
    # pointers to the head and tail nodes of a merged linked list.
    head = None
    tail = None

    while head1 and head2:
        if head1.data <= head2.data:
            if head is None:
                head, tail = head1, head1
            else:
                tail.next = head1
                tail = tail.next
            head1 = head1.next
        else:
            if head is None:
                head, tail = head2, head2
            else:
                tail.next = head2
                tail = tail.next
            head2 = head2.next

    if tail:
        tail.next = head1 or head2
    return head


def merge_sorted_lists_recursive(head1: ListNode, head2: ListNode) -> ListNode:

    def recurse(current1: ListNode, current2: ListNode) -> ListNode:
        # base case: either current1 or current2 is None value.
        if not current1 or not current2:
            # return a non-empty list
            return current1 or current2
        # recursive case: compare two values and make the less node come first
        # then, append the head node of the merged linked list to the less node.

        if current1.data <= current2.data:
            current1.next = recurse(current1.next, current2)
            return current1
        current2.next = recurse(current1, current2.next)
        return current2

    return recurse(head1, head2)


### ZigZag : O(min(n, m))
# where n is the length of the first linked list m is the length of the second linked list
def create_zigzag_list_iterative(head1: ListNode, head2: ListNode) -> ListNode:
    tail = head1
    current1 = head1.next
    current2 = head2
    counter = 0

    while current1 and current2:
        if counter % 2 == 0:
            tail.next = current2
            current2 = current2.next
        else:
            tail.next = current1
            current1 = current1.next
        tail = tail.next
        counter += 1

    if current1:
        tail.next = current1
    if current2:
        tail.next = current2
    return head1


def create_zigzag_list_recursive(head1: ListNode, head2: ListNode) -> ListNode:

    def recurse(current1: ListNode, current2: ListNode) -> ListNode:
        if current1 is None and current2 is None:
            return None
        if current1 is None:
            return current2
        if current2 is None:
            return current1

        next1, next2 = current1.next, current2.next
        current1.next = current2
        current2.next = recurse(next1, next2)
        return current1

    return recurse(head1, head2)


def unique_linked_list(head: ListNode) -> ListNode:
    unique_set = set()
    prev = None
    current = head
    while current:
        if current.data in unique_set:
            prev.next = current.next
        else:
            unique_set.add(current.data)
            prev = current
        current = current.next
    return head


# Reverse the nodes in the specific range [left, right] in a given linked list.
def reverse_between(
    head: Optional[ListNode], left: int, right: int
) -> Optional[ListNode]:
    # First stage: find the previous node of the node at position left.
    left_prev = None
    # tail := the tail node of the reversed linked list, which is the same as the node at position left.
    tail = head
    for _ in range(1, left):
        left_prev = tail
        tail = tail.next

    # Second stage: reverse the sub-list of the range [left, right].
    prev = left_prev
    current = tail
    for _ in range(left, right + 1):
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    # Third stage: link the final node on the left side to the head node of the reversed sub-list.
    if left_prev:
        left_prev.next = prev
    # Also, link the tail node of the reversed sub-list to the first node on the right side.
    if tail:
        tail.next = current
        # when starting with the head node of the given list, return the head node of the reversed list.
        if not left_prev:
            return prev

    return head


# Remove the nodes with the same value as target.
def remove_specific_nodes(
    head: Optional[ListNode], target: object
) -> Optional[ListNode]:
    prev = None
    current = head
    while current:
        next_node = current.next
        if current.data == target:
            if prev:
                prev.next = next_node
            else:
                head = next_node
        else:
            prev = current
        current = next_node
    return head


# Swap pairs
# https://leetcode.com/problems/swap-nodes-in-pairs
def swap_pairs_iterative(head: Optional[ListNode]) -> Optional[ListNode]:
    pass


def swap_pairs_recursive(head: Optional[ListNode]) -> Optional[ListNode]:
    pass


# Split a linked list to k consecutive parts
# https://leetcode.com/problems/split-linked-list-in-parts
def split_list_to_parts(head: Optional[ListNode]) -> Optional[ListNode]:
    pass


# Check if there is a cycle in a linked list.
# https://leetcode.com/problems/linked-list-cycle
def check_cycle(head: Optional[ListNode]) -> Optional[ListNode]:
    pass


# Insert node in a non-decreasing order of circular linked list.
# https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list
def insert_node_into_circular_list(
    head: Optional[ListNode], node: Optional[ListNode]
) -> Optional[ListNode]:
    pass


# Reverse an even length of group.
# https://leetcode.com/problems/reverse-nodes-in-even-length-groups
def reverse_even_length_groups(head: Optional[ListNode]) -> Optional[ListNode]:
    pass

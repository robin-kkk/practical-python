import unittest

from linked_list import LinkedList
from singly_linked_list import SinglyLinkedList
from doubly_linked_list import DoublyLinkedList
import linked_list_utils


class TestLinkedList(unittest.TestCase):

    def assert_linked_list(self, linked_list: LinkedList) -> None:
        tc = [3, 5, 8, 19]
        for i, data in enumerate(tc):
            linked_list.insert(i, data)
        self.assertEqual(linked_list.iterate(), tc)

        linked_list.insert(2, 99)

        for data in [34, 26, 22, 22]:
            linked_list.insert(0, data)
        self.assertEqual(linked_list.iterate(), [22, 22, 26, 34, 3, 5, 99, 8, 19])
        self.assertEqual(linked_list.index(26), 2)
        self.assertEqual(linked_list.index(80), -1)

        for at, expected_result in [(0, 22), (3, 3), (6, 19)]:
            self.assertEqual(linked_list.delete(at).data, expected_result)
        self.assertEqual(linked_list.iterate(), [22, 26, 34, 5, 99, 8])

        while not linked_list.empty():
            linked_list.delete(0)
        self.assertEqual(linked_list.size(), 0)

        linked_list.insert_at_head(44)
        linked_list.insert_at_head(37)
        linked_list.insert_at_tail(56)
        linked_list.insert_at_tail(8)
        self.assertEqual(linked_list.iterate(), [37, 44, 56, 8])

        linked_list.delete_at_tail()
        self.assertEqual(linked_list.iterate(), [37, 44, 56])
        linked_list.delete_at_head()
        self.assertEqual(linked_list.iterate(), [44, 56])

    def test_singly_linked_list(self) -> None:
        sll = SinglyLinkedList()
        self.assert_linked_list(sll)

    def test_doubly_linked_list(self) -> None:
        dll = DoublyLinkedList()
        self.assert_linked_list(dll)

    def test_sum_linked_list(self) -> None:
        # (list, expected_result)
        tc = [4, 5, 8, 1, 3]
        expected_result = sum(tc)

        sll = SinglyLinkedList()
        for data in tc:
            sll.insert_at_head(data)

        result = linked_list_utils.sum_linked_list_iterative(sll.head)
        assert result == expected_result, f"{result} != {expected_result}"
        result = linked_list_utils.sum_linked_list_recursive(sll.head)
        assert result == expected_result, f"{result} != {expected_result}"

    def test_reverse_linked_list(self) -> None:
        tc = [4, 5, 8, 1, 3]
        expected_result = list(reversed(tc))

        sll = linked_list_utils.to_singly_linked_list(tc)
        result = linked_list_utils.reverse_linked_list_iterative(sll.head)
        result = linked_list_utils.to_list(result)
        assert result == expected_result, f"{result} != {expected_result}"

        sll = linked_list_utils.to_singly_linked_list(tc)
        result = linked_list_utils.reverse_linked_list_recursive(sll.head)
        result = linked_list_utils.to_list(result)
        assert result == expected_result, f"{result} != {expected_result}"

    def test_create_zigzag_list(self) -> None:
        tc1 = [7, 8, 1, 3, 9]
        tc2 = [4, 5, 1, 9, 2, 3, 7, 8]
        expected_result = [7, 4, 8, 5, 1, 1, 3, 9, 9, 2, 3, 7, 8]

        list1 = linked_list_utils.to_singly_linked_list(tc1)
        list2 = linked_list_utils.to_singly_linked_list(tc2)
        result = linked_list_utils.create_zigzag_list_iterative(list1.head, list2.head)
        result = linked_list_utils.to_list(result)
        assert result == expected_result, f"{result} != {expected_result}"

        list1 = linked_list_utils.to_singly_linked_list(tc1)
        list2 = linked_list_utils.to_singly_linked_list(tc2)
        result = linked_list_utils.create_zigzag_list_recursive(list1.head, list2.head)
        result = linked_list_utils.to_list(result)
        assert result == expected_result, f"{result} != {expected_result}"

    def test_merge_sorted_lists(self) -> None:
        tc1 = [1, 2, 4]
        tc2 = [1, 3, 4, 4, 7, 9]
        expected_result = sorted(tc1 + tc2)

        list1 = linked_list_utils.to_singly_linked_list(tc1)
        list2 = linked_list_utils.to_singly_linked_list(tc2)
        result = linked_list_utils.merge_sorted_lists_iterative(list1.head, list2.head)
        result = linked_list_utils.to_list(result)
        assert result == expected_result, f"{result} != {expected_result}"

        list1 = linked_list_utils.to_singly_linked_list(tc1)
        list2 = linked_list_utils.to_singly_linked_list(tc2)
        result = linked_list_utils.merge_sorted_lists_recursive(list1.head, list2.head)
        result = linked_list_utils.to_list(result)
        assert result == expected_result, f"{result} != {expected_result}"

    def test_unique_linked_list(self) -> None:
        tc = [1, 1, 3, 4, 5, 2, 2, 7, 8, 7, 9]
        expected_result = [1, 3, 4, 5, 2, 7, 8, 9]

        sll = linked_list_utils.to_singly_linked_list(tc)
        result = linked_list_utils.unique_linked_list(sll.head)
        result = linked_list_utils.to_list(result)
        assert result == expected_result, f"{result} != {expected_result}"

    def test_reverse_between(self) -> None:
        # (list, left, right, expected_result)
        testcases = [
            ([1], 1, 1, [1]),
            ([1, 3, 5], 2, 3, [1, 5, 3]),
            ([1, 3, 5], 1, 2, [3, 1, 5]),
            ([1, 3, 5, 7], 1, 4, [7, 5, 3, 1]),
        ]
        for tc, left, right, expected_result in testcases:
            sll = linked_list_utils.to_singly_linked_list(tc)
            result = linked_list_utils.reverse_between(sll.head, left, right)
            result = linked_list_utils.to_list(result)
            assert result == expected_result, f"{result} != {expected_result}"

    def test_remove_specific_nodes(self) -> None:
        # (list, target, expected_result)
        testcases = [
            ([1], 1, []),
            ([1, 3, 4, 3], 3, [1, 4]),
            ([5, 7, 5, 5, 3, 5, 2], 5, [7, 3, 2]),
        ]
        for tc, target, expected_result in testcases:
            sll = linked_list_utils.to_singly_linked_list(tc)
            result = linked_list_utils.remove_specific_nodes(sll.head, target)
            result = linked_list_utils.to_list(result)
            assert result == expected_result, f"{result} != {expected_result}"


if __name__ == "__main__":
    unittest.main()

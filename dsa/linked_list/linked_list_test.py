import unittest

from linked_list import LinkedList
from singly_linked_list import SinglyLinkedList
from doubly_linked_list import DoublyLinkedList


class TestLinkedList(unittest.TestCase):

    def assert_linked_list(self, linked_list: LinkedList) -> None:
        tc = [3, 5, 8, 19]
        for i, data in enumerate(tc):
            linked_list.insert(i, data)
        self.assertEqual(linked_list.iterate(), tc)

        for data in [34, 26, 22, 22]:
            linked_list.insert(0, data)
        self.assertEqual(linked_list.iterate(), [22, 22, 26, 34, 3, 5, 8, 19])
        self.assertEqual(linked_list.index(26), 2)
        self.assertEqual(linked_list.index(80), -1)

        for at, expected_result in [(0, 22), (3, 3), (5, 19)]:
            self.assertEqual(linked_list.delete(at).data, expected_result)
        self.assertEqual(linked_list.iterate(), [22, 26, 34, 5, 8])

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


if __name__ == "__main__":
    unittest.main()

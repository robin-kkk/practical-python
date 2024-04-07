import unittest

from queue import Queue, ListQueue
import queue_utils


class TestQueue(unittest.TestCase):
    def test_queue(self) -> None:
        queue = Queue()
        for elem in ["1", "2", "3", "4"]:
            queue.enqueue(elem)
        assert queue.peek_front() == "1"
        assert queue.peek_back() == "4"
        assert queue.contain("3") is True
        assert queue.remove("3") is True
        assert queue.remove("10") is False
        assert queue.dequeue() == "1"
        assert queue.dequeue() == "2"
        assert queue.dequeue() == "4"

    def test_list_queue(self) -> None:
        queue = ListQueue()
        for elem in ["1", "2", "3", "4"]:
            queue.enqueue(elem)
        assert queue.peek_front() == "1"
        assert queue.peek_back() == "4"
        assert queue.contain("3") is True
        assert queue.remove("3") is True
        assert queue.remove("10") is False
        assert queue.dequeue() == "1"
        assert queue.dequeue() == "2"
        assert queue.dequeue() == "4"
    
    def test_get_monotonic_increasing_stack(self) -> None:
        # (arr, expected_result)
        tc = [
            ([3, 2, 4, 1, 5, 7], [1, 5, 7]),
            ([2, 5, 3, 8, 7], [2, 3, 7]),
        ]

        for arr, expected_result in tc:
            assert queue_utils.get_monotonic_increasing_deque(arr) == expected_result

    def test_get_monotonic_decreasing_stack(self) -> None:
        # (arr, expected_result)
        tc = [
            ([3, 2, 4, 7, 5, 1], [7, 5, 1]),
            ([6, 4, 7, 1, 8, 3], [8, 3]),
        ]

        for arr, expected_result in tc:
            assert queue_utils.get_monotonic_decreasing_deque(arr) == expected_result


if __name__ == "__main__":
    unittest.main()

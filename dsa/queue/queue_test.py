import unittest

from queue import Queue, ListQueue


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


if __name__ == "__main__":
    unittest.main()

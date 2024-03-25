from collections import deque


class Queue:
    def __init__(self) -> None:
        self._linear_ds = deque()
        self._front = 0
        self._back = -1

    def size(self) -> int:
        return self._back + 1

    def is_empty(self) -> bool:
        return self._back == -1

    def peek_front(self) -> object:
        if self.is_empty():
            raise Exception("Queue is empty.")
        return self._linear_ds[self._front]

    def peek_back(self) -> object:
        if self.is_empty():
            raise Exception("Queue is empty.")
        return self._linear_ds[self._back]

    def enqueue(self, data: object) -> None:
        self._linear_ds.append(data)
        self._back += 1

    def dequeue(self) -> object:
        if self.is_empty():
            raise Exception("Queue is empty.")
        self._back -= 1
        return self._linear_ds.popleft()  # O(1)

    def contain(self, data: object) -> bool:
        return data in self._linear_ds  # O(n)

    def remove(self, data: object) -> bool:
        if self.contain(data):
            self._back -= 1
            self._linear_ds.remove(data)  # O(n)
            return True
        return False


""" ListQueue is implemented by a doubly linked list. """


class ListNode:
    def __init__(self, data: object) -> None:
        self.reset()
        self.data = data

    def reset(self) -> None:
        self.data = None
        self.prev = None
        self.next = None


class ListQueue:
    def __init__(self) -> None:
        # _front refers to the node that corresponds to the element at the front of a queue.
        self._front = None
        # _back refers to the node that corresponds to the element at the back of a queue.
        self._back = None
        self._size = 0

    def size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def peek_front(self) -> object:
        if self._front is None:
            raise Exception("Queue must not be empty.")
        return self._front.data

    def peek_back(self) -> object:
        if self._back is None:
            raise Exception("Queue must not be empty.")
        return self._back.data

    def enqueue(self, data: object) -> None:
        node = ListNode(data)
        if self._back is None:
            self._front, self._back = node, node
        else:
            node.prev = self._back
            self._back.next = node
            self._back = node
        self._size += 1

    def dequeue(self) -> object:
        if self._front is None:
            raise Exception("Queue must not be empty.")

        node = self._front
        ret = node.data
        if self._front.next:
            self._front.next.prev = None
            self._front = self._front.next
        node.reset()
        del node
        self._size -= 1
        return ret

    # O(n)
    def contain(self, data: object) -> bool:
        node = self._front
        while node:
            if node.data == data:
                return True
            node = node.next
        return False

    # O(n)
    def remove(self, data: object) -> bool:
        node = self._back
        while node:
            if node.data == data:
                break
            node = node.prev

        if node is None:
            return False

        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        node.reset()
        del node
        self._size -= 1
        return True

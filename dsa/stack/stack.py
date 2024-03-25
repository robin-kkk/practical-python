""" This simple stack is implemented by an array. """


class Stack:
    def __init__(self) -> None:
        self._linear_ds = []
        # The index of the top of a stack which always refers to the last one.
        self._top = -1

    def size(self) -> int:
        return self._top + 1

    def is_empty(self) -> bool:
        return self._top == -1

    def peek(self) -> object:
        if self.is_empty():
            raise Exception("Stack must not be empty.")
        return self._linear_ds[self._top]

    def push(self, data: object) -> None:
        self._linear_ds.append(data)
        self._top += 1

    def pop(self) -> object:
        if self.is_empty():
            raise Exception("Stack must not be empty.")
        self._top -= 1
        return self._linear_ds.pop()

    def contain(self, data: object) -> bool:
        return data in self._linear_ds  # O(n)

    def remove(self, data: object) -> bool:
        # O(n)
        tmp = []
        while not self.is_empty():
            elem = self.pop()
            if elem == data:
                self._linear_ds.extend(tmp[::-1])
                self._top += len(tmp)
                return True
            tmp.append(elem)
        self._top += len(tmp)
        self._linear_ds = tmp[::-1]
        return False


""" ListStack is implemented by a doubly linked list. """


class ListNode:
    def __init__(self, data: object) -> None:
        self.reset()
        self.data = data

    def reset(self) -> None:
        self.data = None
        self.prev = None
        self.next = None


class ListStack:
    def __init__(self) -> None:
        self._tail = None
        self._size = 0

    def size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def peek(self) -> object:
        if self._tail is None:
            raise Exception("Stack must not be empty.")
        return self._tail.data

    def push(self, data: object) -> None:
        node = ListNode(data)
        if self._tail is None:
            self._tail = node
        else:
            node.prev = self._tail
            self._tail.next = node
            self._tail = node
        self._size += 1
        return None

    def pop(self) -> object:
        if self._tail is None:
            raise Exception("Stack must not be empty.")

        node = self._tail
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        self._tail = node.prev
        self._size -= 1
        ret = node.data
        node.reset()
        del node
        return ret

    # O(n)
    def contain(self, data: object) -> bool:
        node = self._tail
        while node:
            if node.data == data:
                return True
            node = node.prev
        return False

    # O(n)
    def remove(self, data: object) -> bool:
        node = self._tail
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
        if self._size == 1:
            self._tail = None
        node.reset()
        del node
        self._size -= 1
        return True

    def iterate(self) -> list[object]:
        ret = []
        node = self._tail
        while node:
            ret.append(node.data)
            node = node.prev
        return ret[::-1]

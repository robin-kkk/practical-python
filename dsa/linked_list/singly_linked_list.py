from linked_list import ListNode, LinkedList


class SllNode(ListNode):
    def __init__(self, data: object) -> None:
        super().__init__(data)
        self.next = None

    def reset(self) -> None:
        self.next = None


class SinglyLinkedList(LinkedList):
    def __init__(self) -> None:
        self._size = 0
        self.head = None
        self.tail = None

    def empty(self) -> bool:
        return self._size == 0

    def size(self) -> int:
        return self._size

    def index(self, data: object) -> int:
        i = 0
        node = self.head
        while node:
            if node.data == data:
                return i
            i += 1
            node = node.next
        return -1

    def search_by_index(self, at: int) -> ListNode:
        node = self.head
        for i in range(self._size):
            if i == at:
                return node
            node = node.next
        return None

    def search(self, data: object) -> ListNode:
        node = self.head
        while node:
            if node.data == data:
                return node
            node = node.next
        return None

    def insert_at_head(self, data: object) -> None:
        node = SllNode(data)
        if self.head is None:
            self.head, self.tail = node, node
        else:
            node.next = self.head
            self.head = node
        self._size += 1
        return None

    def insert_at_tail(self, data: object) -> None:
        node = SllNode(data)
        if self.tail is None:
            self.head, self.tail = node, node
        else:
            self.tail.next = node
            self.tail = node
        self._size += 1
        return None

    def insert(self, at: int, data: object) -> None:
        if at > self._size:
            raise Exception(f"cannot insert at index {at}.")

        if at == 0:
            return self.insert_at_head(data)
        elif at == self._size:
            return self.insert_at_tail(data)

        # Insert in the middle.
        node = SllNode(data)
        prev_node = self.search_by_index(at - 1)
        node.next = prev_node.next
        prev_node.next = node
        self._size += 1
        return None

    def delete_at_head(self) -> ListNode:
        if self.head is None:
            raise Exception("list must not be empty.")

        if self.head == self.tail:
            self.tail = None
        deleted = self.head
        self.head = self.head.next
        deleted.reset()
        self._size -= 1
        return deleted

    def delete_at_tail(self) -> ListNode:
        if self.tail is None:
            raise Exception("list must not be empty.")

        if self.head == self.tail:
            self.head = None
        deleted = self.tail
        prev_node = self.search_by_index(self._size - 2)
        self.tail = prev_node
        if self.tail:
            self.tail.next = None
        deleted.reset()
        self._size -= 1
        return deleted

    def delete(self, at: int) -> ListNode:
        if at >= self._size:
            raise Exception(f"cannot delete at index {at}.")

        if at == 0:
            return self.delete_at_head()
        elif at == self._size - 1:
            return self.delete_at_tail()

        # Delete in the middle.
        prev_node = self.search_by_index(at - 1)
        deleted = prev_node.next
        prev_node.next = deleted.next
        deleted.reset()
        self._size -= 1
        return deleted

    def iterate(self) -> list[object]:
        objects = []
        node = self.head
        while node:
            objects.append(node.data)
            node = node.next
        return objects

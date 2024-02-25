import abc


class ListNode:
    def __init__(self, data: object) -> None:
        self.data = data


class LinkedList(abc.ABC):
    @abc.abstractmethod
    def empty(self) -> bool:
        raise NotImplementedError

    @abc.abstractmethod
    def size(self) -> int:
        raise NotImplementedError

    @abc.abstractmethod
    def index(self, data: object) -> int:
        raise NotImplementedError

    @abc.abstractmethod
    def search_by_index(self, at: int) -> ListNode:
        raise NotImplementedError

    @abc.abstractmethod
    def search(self, data: object) -> ListNode:
        raise NotImplementedError

    @abc.abstractmethod
    def insert_at_head(self, data: object) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def insert_at_tail(self, data: object) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def insert(self, at: int, data: object) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def delete_at_head(self) -> ListNode:
        raise NotImplementedError

    @abc.abstractmethod
    def delete_at_tail(self) -> ListNode:
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, at: int) -> ListNode:
        raise NotImplementedError

    @abc.abstractmethod
    def iterate(self) -> list[object]:
        raise NotImplementedError

from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class ListNode(Generic[T]):
    """
    Tek yönlü bağlı liste düğümü (Singly Linked List Node).
    """

    def __init__(self, val: T, next_node: Optional["ListNode[T]"] = None) -> None:
        self.val = val
        self.next = next_node

    def __repr__(self) -> str:
        return f"ListNode({self.val})"


class LinkedList(Generic[T]):
    """
    Tek Yönlü Bağlı Liste (Singly Linked List).
    Dizilerden farklı olarak ardışık hafıza gerektirmez; düğümler işaretçilerle (pointers) birbirine bağlanır.
    """

    def __init__(self) -> None:
        self.head: Optional[ListNode[T]] = None
        self._size: int = 0

    def append(self, val: T) -> None:
        """Listenin sonuna yeni bir eleman ekler - O(N) zaman."""
        new_node = ListNode(val)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
        self._size += 1

    def prepend(self, val: T) -> None:
        """Listenin başına yeni bir eleman ekler - O(1) zaman."""
        new_node = ListNode(val, self.head)
        self.head = new_node
        self._size += 1

    def to_list(self) -> list[T]:
        """Bağlı listeyi standart Python listesine çevirir - O(N) zaman."""
        result: list[T] = []
        curr = self.head
        while curr is not None:
            result.append(curr.val)
            curr = curr.next
        return result

    @classmethod
    def from_list(cls, items: list[T]) -> "LinkedList[T]":
        """Python listesinden bağlı liste inşa eden fabrika metodu."""
        ll = cls()
        for item in items:
            ll.append(item)
        return ll

    def is_empty(self) -> bool:
        return self.head is None

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        items = " -> ".join(str(v) for v in self.to_list())
        return f"LinkedList({items if items else 'Empty'})"

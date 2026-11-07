from typing import Generic, TypeVar

T = TypeVar("T")


class Stack(Generic[T]):
    """
    OOP Encapsulation & Generic TypeVar:
    LIFO (Last In, First Out) Yığın Veri Yapısı.
    
    Tüm temel işlemler O(1) zaman karmaşıklığında çalışır.
    """
    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        """Yığının en tepesine yeni bir eleman ekler. Zaman Karmaşıklığı: O(1)"""
        self._items.append(item)

    def pop(self) -> T:
        """
        Yığının en tepesindeki elemanı çıkarır ve döner.
        Zaman Karmaşıklığı: O(1)
        """
        if self.is_empty():
            raise IndexError("Boş bir yığından (Stack) eleman çıkarılamaz!")
        return self._items.pop()

    def peek(self) -> T:
        """
        En tepedeki elemanı yığından çıkarmadan sadece görüntüler.
        Zaman Karmaşıklığı: O(1)
        """
        if self.is_empty():
            raise IndexError("Boş bir yığının tepesine bakılamaz!")
        return self._items[-1]

    def is_empty(self) -> bool:
        """Yığın boş mu kontrol eder. Zaman Karmaşıklığı: O(1)"""
        return len(self._items) == 0

    def size(self) -> int:
        """Yığındaki toplam eleman sayısını döner. Zaman Karmaşıklığı: O(1)"""
        return len(self._items)

    def __repr__(self) -> str:
        return f"Stack({self._items})"

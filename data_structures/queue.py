from collections import deque
from typing import Generic, TypeVar

T = TypeVar("T")


class Queue(Generic[T]):
    """
    OOP Encapsulation & Generic Type:
    FIFO (First In, First Out) Kuyruk Veri Yapısı.
    
    Python'ın optimize edilmiş 'deque' çift uçlu kuyruğunu kullanarak
    kuyruğa ekleme ve baştan çıkarma işlemlerini O(1) hızında yapar.
    """
    def __init__(self) -> None:
        self._items: deque[T] = deque()

    def enqueue(self, item: T) -> None:
        """Kuyruğun sonuna yeni bir eleman ekler. Zaman Karmaşıklığı: O(1)"""
        self._items.append(item)

    def dequeue(self) -> T:
        """
        Kuyruğun en başındaki (ilk giren) elemanı çıkarır ve döner.
        Zaman Karmaşıklığı: O(1)
        """
        if self.is_empty():
            raise IndexError("Boş bir kuyruktan (Queue) eleman çıkarılamaz!")
        return self._items.popleft()

    def front(self) -> T:
        """
        Kuyruğun en başındaki elemanı çıkarmadan sadece görüntüler.
        Zaman Karmaşıklığı: O(1)
        """
        if self.is_empty():
            raise IndexError("Boş bir kuyruğun önüne bakılamaz!")
        return self._items[0]

    def is_empty(self) -> bool:
        """Kuyruk boş mu kontrol eder. Zaman Karmaşıklığı: O(1)"""
        return len(self._items) == 0

    def size(self) -> int:
        """Kuyruktaki toplam eleman sayısını döner. Zaman Karmaşıklığı: O(1)"""
        return len(self._items)

    def __repr__(self) -> str:
        return f"Queue({list(self._items)})"

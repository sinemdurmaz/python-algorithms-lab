from typing import Optional, TypeVar
from data_structures.linked_list import ListNode

T = TypeVar("T")


def has_cycle(head: Optional[ListNode[T]]) -> bool:
    """
    LeetCode #141: Linked List Cycle (Bağlı Listede Döngü Tespiti)

    Bir bağlı listede sonsuz döngü olup olmadığını Floyd'un
    Kaplumbağa ve Tavşan (Tortoise and Hare / Fast & Slow Pointers)
    algoritmasıyla tespit eder.

    Algoritma Tekniği: Hızlı ve Yavaş İşaretçiler (Fast & Slow Pointers)
    Zaman Karmaşıklığı: O(N) - Liste uzunluğu boyunca en fazla birkaç turda kesişim gerçekleşir.
    Alan Karmaşıklığı: O(1) - Küme (HashSet) kullanmadan sabit iki işaretçiyle çalışır.
    """
    if head is None or head.next is None:
        return False

    slow: Optional[ListNode[T]] = head
    fast: Optional[ListNode[T]] = head

    while fast is not None and fast.next is not None:
        slow = slow.next          # 1 adım ilerler (Kaplumbağa)
        fast = fast.next.next     # 2 adım ilerler (Tavşan)

        if slow is fast:
            return True           # Döngü tespit edildi!

    return False                  # fast listenin sonuna (None) ulaştı, döngü yok

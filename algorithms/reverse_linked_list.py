from typing import Optional, TypeVar
from data_structures.linked_list import ListNode

T = TypeVar("T")


def reverse_linked_list(head: Optional[ListNode[T]]) -> Optional[ListNode[T]]:
    """
    LeetCode #206: Reverse Linked List (Bağlı Listeyi Tersine Çevirme)

    Verilen tek yönlü bağlı listenin yönünü in-place (yerinde) tersine çevirir.
    Örnek: 1 -> 2 -> 3 -> 4 -> 5 -> None  ==>  5 -> 4 -> 3 -> 2 -> 1 -> None

    Algoritma Tekniği: Üç İşaretçi İterasyonu (prev, curr, next_node)
    Zaman Karmaşıklığı: O(N) - Her düğüm tam olarak bir kez ziyaret edilir.
    Alan Karmaşıklığı: O(1) - Yeni düğümler tahsis edilmez, var olan işaretçiler ters çevrilir.
    """
    prev: Optional[ListNode[T]] = None
    curr: Optional[ListNode[T]] = head

    while curr is not None:
        next_node = curr.next  # 1. Gelecek düğümün referansını kaybetmemek için sakla
        curr.next = prev       # 2. Düğümün işaretçisini geriye (prev'e) çevir
        prev = curr            # 3. prev işaretçisini bir adım ileri taşı
        curr = next_node       # 4. curr işaretçisini bir sonraki düğüme taşı

    return prev

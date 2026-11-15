from typing import Optional, TypeVar
from data_structures.linked_list import ListNode

T = TypeVar("T")


def merge_two_sorted_lists(
    list1: Optional[ListNode[T]], list2: Optional[ListNode[T]]
) -> Optional[ListNode[T]]:
    """
    LeetCode #21: Merge Two Sorted Lists (İki Sıralı Bağlı Listeyi Birleştirme)

    Sıralı iki tek yönlü bağlı listeyi, tek bir sıralı bağlı liste halinde
    var olan düğüm işaretçilerini birbirine bağlayarak (splice) birleştirir.

    Algoritma Tekniği: Sahte Baş Düğüm (Dummy Head) & İki İşaretçi
    Zaman Karmaşıklığı: O(N + M) - İki listenin toplam uzunluğu kadar adım atılır.
    Alan Karmaşıklığı: O(1) - Yeni düğüm tahsis edilmez, var olan referanslar bağlanır.
    """
    dummy = ListNode(None)  # Edge-case kontrollerini sadeleştiren sahte baş düğüm
    tail = dummy

    while list1 is not None and list2 is not None:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    # Kalan düğümleri doğrudan listenin sonuna iliştir
    tail.next = list1 if list1 is not None else list2

    return dummy.next

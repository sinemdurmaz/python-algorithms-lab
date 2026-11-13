import pytest
from data_structures.linked_list import LinkedList, ListNode
from algorithms.reverse_linked_list import reverse_linked_list


def test_linked_list_basic_operations():
    """Bağlı listenin temel operasyonlarını (append, prepend, size, to_list) test eder."""
    ll = LinkedList[int]()
    assert ll.is_empty() is True
    assert len(ll) == 0
    assert ll.to_list() == []

    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert ll.is_empty() is False
    assert len(ll) == 3
    assert ll.to_list() == [1, 2, 3]

    ll.prepend(0)
    assert len(ll) == 4
    assert ll.to_list() == [0, 1, 2, 3]
    assert "LinkedList(0 -> 1 -> 2 -> 3)" in repr(ll)


def test_linked_list_from_list_factory():
    """from_list fabrika metodunun doğruluğunu test eder."""
    ll = LinkedList.from_list([10, 20, 30])
    assert len(ll) == 3
    assert ll.to_list() == [10, 20, 30]


@pytest.mark.parametrize("initial_list, expected_reversed", [
    ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),  # Standart liste
    ([1, 2], [2, 1]),                    # İki elemanlı liste
    ([42], [42]),                        # Tek elemanlı liste
    ([], []),                            # Boş liste
    ([10, 20, 30, 40], [40, 30, 20, 10]),# Dört elemanlı liste
    (["x", "y", "z"], ["z", "y", "x"]),  # String generic desteği
])
def test_reverse_linked_list(initial_list: list, expected_reversed: list):
    """LeetCode #206 Bağlı listeyi tersine çevirme senaryolarını test eder."""
    ll = LinkedList.from_list(initial_list)
    new_head = reverse_linked_list(ll.head)

    # Yeni head üzerinden listeyi topla
    result = []
    curr = new_head
    while curr is not None:
        result.append(curr.val)
        curr = curr.next

    assert result == expected_reversed

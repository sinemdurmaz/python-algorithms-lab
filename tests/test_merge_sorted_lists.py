import pytest
from data_structures.linked_list import LinkedList, ListNode
from algorithms.merge_sorted_lists import merge_two_sorted_lists


@pytest.mark.parametrize("vals1, vals2, expected", [
    ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),          # Klasik LeetCode #21 örneği
    ([], [0], [0]),                                      # Biri boş
    ([], [], []),                                        # İkisi de boş
    ([1, 5, 9], [2, 3, 4, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8, 9]), # Farklı uzunluklar
    ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6]),          # Bir liste tamamen küçük
    ([-10, -5, 0], [-7, -2, 5], [-10, -7, -5, -2, 0, 5]), # Negatif sayılar
    ([2, 2, 2], [2, 2], [2, 2, 2, 2, 2]),                # Tamamen yinelenen değerler
])
def test_merge_two_sorted_lists(vals1: list[int], vals2: list[int], expected: list[int]):
    """LeetCode #21 İki sıralı bağlı listeyi birleştirme senaryolarını test eder."""
    ll1 = LinkedList.from_list(vals1)
    ll2 = LinkedList.from_list(vals2)

    merged_head = merge_two_sorted_lists(ll1.head, ll2.head)

    # Sonucu Python listesine dönüştür
    result = []
    curr = merged_head
    while curr is not None:
        result.append(curr.val)
        curr = curr.next

    assert result == expected

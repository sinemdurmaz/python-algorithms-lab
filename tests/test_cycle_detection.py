import pytest
from data_structures.linked_list import ListNode, LinkedList
from algorithms.has_cycle import has_cycle


def create_linked_list_with_cycle(values: list[int], pos: int) -> ListNode[int] | None:
    """
    Test yardımcısı: Verilen değerlerden bağlı liste oluşturur ve
    pos >= 0 ise son elemanın next işaretçisini o indeksteki düğüme bağlayarak döngü oluşturur.
    """
    if not values:
        return None

    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    if pos >= 0 and pos < len(nodes):
        nodes[-1].next = nodes[pos]

    return nodes[0]


@pytest.mark.parametrize("values, pos, expected", [
    ([3, 2, 0, -4], 1, True),   # Klasik LeetCode #141 döngülü senaryo
    ([1, 2], 0, True),          # İki elemanlı döngü
    ([1], -1, False),           # Tek eleman, döngü yok
    ([1], 0, True),             # Tek eleman kendi kendine dönüyor (Self-loop)
    ([], -1, False),            # Boş liste
    ([1, 2, 3, 4, 5], -1, False), # Düz doğrusal liste
    (list(range(50)), 20, True),  # Uzun liste, ortada döngü
    (list(range(50)), -1, False), # Uzun liste, döngü yok
])
def test_has_cycle_scenarios(values: list[int], pos: int, expected: bool):
    """LeetCode #141 Floyd Döngü Tespiti senaryolarını test eder."""
    head = create_linked_list_with_cycle(values, pos)
    assert has_cycle(head) == expected

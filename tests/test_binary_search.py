import pytest
from algorithms.binary_search import binary_search


@pytest.mark.parametrize("nums, target, expected", [
    ([-1, 0, 3, 5, 9, 12], 9, 4),      # Ortada bulunan
    ([-1, 0, 3, 5, 9, 12], 2, -1),     # Listede olmayan
    ([-1, 0, 3, 5, 9, 12], -1, 0),     # İlk eleman
    ([-1, 0, 3, 5, 9, 12], 12, 5),     # Son eleman
    ([5], 5, 0),                       # Tek elemanlı başarılı
    ([5], -5, -1),                     # Tek elemanlı başarısız
    ([], 1, -1),                       # Boş liste
    ([1, 2, 3, 4, 5, 6, 7, 8], 1, 0),  # Çift sayıda eleman
])
def test_binary_search_scenarios(nums: list[int], target: int, expected: int):
    """LeetCode #704 İkili arama senaryolarını test eder."""
    assert binary_search(nums, target) == expected

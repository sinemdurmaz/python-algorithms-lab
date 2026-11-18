import pytest
from algorithms.contains_duplicate import contains_nearby_duplicate


@pytest.mark.parametrize("nums, k, expected", [
    ([1, 2, 3, 1], 3, True),            # Klasik LeetCode #219 (i=0, j=3, diff=3 <= 3)
    ([1, 0, 1, 1], 1, True),            # Çoklu tekrar, mesafe 1
    ([1, 2, 3, 1, 2, 3], 2, False),     # Tüm tekrarlar mesafe 3'te (> 2)
    ([], 0, False),                     # Boş liste
    ([1], 1, False),                    # Tek eleman
    ([-1, -1], 1, True),                # Negatif sayılar
    ([1, 2, 1], 0, False),              # k=0 (farklı indeks kuralı gereği False)
    ([99, 99], 2, True),                # İki eleman, k mesafesi içinde
])
def test_contains_nearby_duplicate(nums: list[int], k: int, expected: bool):
    """LeetCode #219 Contains Duplicate II senaryolarını test eder."""
    assert contains_nearby_duplicate(nums, k) == expected

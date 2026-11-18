import pytest
from algorithms.max_average_subarray import find_max_average


@pytest.mark.parametrize("nums, k, expected", [
    ([1, 12, -5, -6, 50, 3], 4, 12.75),       # Klasik LeetCode #643 örneği (51 / 4)
    ([5], 1, 5.0),                            # Tek elemanlı dizi
    ([0, 4, 0, 3, 2], 1, 4.0),                 # Tek boyutlu pencere
    ([-1, -2, -3, -4], 2, -1.5),              # Negatif sayılar (-3 / 2)
    ([1, 2, 3], 3, 2.0),                      # k dizinin tamamına eşit
    ([4, 2, 1, 3, 3], 2, 3.0),                # Çoklu tepe noktaları
])
def test_find_max_average_scenarios(nums: list[int], k: int, expected: float):
    """LeetCode #643 Maksimum Ortalama Alt Dizi senaryolarını test eder."""
    assert find_max_average(nums, k) == pytest.approx(expected, 0.0001)


def test_find_max_average_invalid_inputs():
    """Hatalı giriş durumlarında ValueError fırlatıldığını doğrular."""
    with pytest.raises(ValueError):
        find_max_average([1, 2], 5)

    with pytest.raises(ValueError):
        find_max_average([1, 2, 3], 0)

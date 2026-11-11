import pytest
from algorithms.buy_sell_stock import max_profit


@pytest.mark.parametrize("prices, expected", [
    ([7, 1, 5, 3, 6, 4], 5),       # 1'den al, 6'dan sat -> Kâr = 5
    ([7, 6, 4, 3, 1], 0),          # Sürekli düşen piyasa -> Alım yapılmaz, kâr = 0
    ([2, 4, 1], 2),                # 2'den al 4'ten sat -> Kâr = 2 (1'den sonra satış günü yok)
    ([1, 2], 1),                   # İki günlük basit artış -> Kâr = 1
    ([1], 0),                      # Tek günlük fiyat -> Kâr = 0
    ([], 0),                       # Boş liste -> Kâr = 0
    ([3, 3, 3, 3], 0),             # Sabit fiyat -> Kâr = 0
    ([2, 1, 2, 0, 1], 1),          # Çoklu dip senaryosu -> Kâr = 1
    ([1, 2, 3, 4, 5], 4),          # Sürekli yükselen ralli -> Kâr = 4
])
def test_max_profit_scenarios(prices: list[int], expected: int):
    """LeetCode #121 Hisse senedi alım-satım kâr senaryolarını test eder."""
    assert max_profit(prices) == expected

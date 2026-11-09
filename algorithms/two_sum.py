def two_sum(nums: list[int], target: int) -> list[int]:
    """
    LeetCode #1: Two Sum (İki Sayının Toplamı)
    
    Verilen 'nums' dizisinde toplamları 'target' değerine eşit olan
    iki farklı elemanın indekslerini döner.
    
    Veri Yapısı: Hash Map (Python Dict)
    Zaman Karmaşıklığı: O(N) - Liste tek bir döngüde taranır.
    Alan Karmaşıklığı: O(N) - Ziyaret edilen sayılar ve indeksleri sözlükte saklanır.
    """
    seen: dict[int, int] = {}  # {sayı: indeks} hafıza tablosu

    for index, num in enumerate(nums):
        complement = target - num  # Hedefe ulaşmak için gereken tamamlayıcı sayı

        # Aradığımız sayı daha önce sözlüğe kaydedilmişse eşleşmeyi bulduk!
        if complement in seen:
            return [seen[complement], index]

        # Henüz eşleşme yoksa şu anki sayıyı ve indeksini sözlüğe kaydet
        seen[num] = index

    return []

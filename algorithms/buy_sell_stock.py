def max_profit(prices: list[int]) -> int:
    """
    LeetCode #121: Best Time to Buy and Sell Stock (Hisse Kâr Maksimizasyonu)
    
    Verilen hisse fiyatları listesinde tek bir alım ve satım işlemiyle
    elde edilebilecek maksimum kârı hesaplar. Kâr elde edilemiyorsa 0 döner.
    
    Algoritma Tekniği: Tek Geçiş (One-Pass / Greedy)
    Zaman Karmaşıklığı: O(N) - Liste baştan sona yalnızca bir kez taranır.
    Alan Karmaşıklığı: O(1) - Yalnızca iki sayı değişkeni (min_price, maximum_profit) tutulur.
    """
    if not prices:
        return 0

    min_price = float("inf")
    maximum_profit = 0

    for price in prices:
        # 1. Şu ana kadarki en ucuz alım gününü güncelle
        if price < min_price:
            min_price = price
        # 2. Bugün satılsaydı elde edilecek kâr rekor kırıyor mu?
        elif price - min_price > maximum_profit:
            maximum_profit = price - min_price

    return int(maximum_profit)

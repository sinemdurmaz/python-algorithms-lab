def is_palindrome(s: str) -> bool:
    """
    LeetCode #125: Valid Palindrome (Geçerli Palindrom Kontrolü)

    Verilen metnin alfasayısal karakterlerinin (harfler ve rakamlar)
    büyük/küçük harf duyarsız olarak baştan ve sondan aynı okunup
    okunmadığını kontrol eder.

    Algoritma Tekniği: İki İşaretçi (Two Pointers)
    Zaman Karmaşıklığı: O(N) - Metin her iki uçtan merkeze doğru tek sefer taranır.
    Alan Karmaşıklığı: O(1) - Yeni bir dizi veya filtrelenmiş string üretilmez,
                             işaretçiler doğrudan orijinal metin üzerinde hareket eder.
    """
    left = 0
    right = len(s) - 1

    while left < right:
        # Sol işaretçiyi alfasayısal olmayan karakterleri atlayarak ilerlet
        while left < right and not s[left].isalnum():
            left += 1

        # Sağ işaretçiyi alfasayısal olmayan karakterleri atlayarak gerilet
        while left < right and not s[right].isalnum():
            right -= 1

        # Harfleri küçük harfe çevirerek karşılaştır
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True

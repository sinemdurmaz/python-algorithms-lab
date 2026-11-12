import pytest
from algorithms.valid_palindrome import is_palindrome


@pytest.mark.parametrize("s, expected", [
    ("A man, a plan, a canal: Panama", True),  # Klasik noktalama ve boşluklu LeetCode senaryosu
    ("race a car", False),                     # Palindrom olmayan string
    (" ", True),                               # Yalnızca boşluk
    ("", True),                                # Boş string
    (".,?! ;:", True),                         # Sadece noktalama işaretleri
    ("a", True),                               # Tek karakter
    ("aa", True),                              # İki aynı karakter
    ("ab", False),                             # İki farklı karakter
    ("0P", False),                             # Sayı ve harf uyuşmazlığı
    ("1221", True),                            # Tamamen sayılardan oluşan çift palindrom
    ("1a2b2a1", True),                         # Sayı ve harf karışık palindrom
    ("Was it a car or a cat I saw?", True),    # Uzun soru cümlesi
    ("...aba...", True),                       # Uçlarda noktalama işaretleri
    ("kayak", True),                           # Tek sayılı klasik palindrom kelime
    ("noon", True),                            # Çift sayılı klasik palindrom kelime
    ("ab_a", True),                            # Alt çizgi (underscore) alfasayısal değildir
])
def test_valid_palindrome_scenarios(s: str, expected: bool):
    """LeetCode #125 Valid Palindrome Two Pointers test senaryolarını doğrular."""
    assert is_palindrome(s) == expected

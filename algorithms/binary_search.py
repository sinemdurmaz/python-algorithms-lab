def binary_search(nums: list[int], target: int) -> int:
    """
    LeetCode #704: Binary Search (İkili Arama)
    
    Sıralı (ascending) bir 'nums' listesinde 'target' değerini arar.
    Eleman bulunursa indeksini, bulunamazsa -1 döner.
    
    Algoritma Tekniği: Böl ve Yönet (Divide and Conquer)
    Zaman Karmaşıklığı: O(log N) - Her adımda arama uzayı yarıya iner.
    Alan Karmaşıklığı: O(1) - Yalnızca iki işaretçi (left, right) kullanılır.
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        # Orta indeksi hesapla (integer division)
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            # Aranan sayı sağ yarıda, sol sınırı kaydır
            left = mid + 1
        else:
            # Aranan sayı sol yarıda, sağ sınırı kaydır
            right = mid - 1

    return -1
